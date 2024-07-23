from datetime import timedelta
from django.utils import timezone
import random
from .models import DEFAULT_V_CODE
from home.settings import SIMPLECAPTCHA_DURATION

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .permissions import IsPhoneOwnerPermission


class PhoneViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsPhoneOwnerPermission)

        

    # @action(methods=['post'])
    # def verify(self, request, *args, **kwargs):
        # v_code = request.data.get('v_code')

        # if not v_code: # validation
        #     return Response({'error': 'Bad request. v_code is required'}, 
        #                         status=status.HTTP_400_BAD_REQUEST)

        # pre = request.data.get('pre')

        # if not pre: # validation
        #     return Response({'error': 'Bad request. phone prefix(pre) is required'}, 
        #                         status=status.HTTP_400_BAD_REQUEST)

        # no = request.data.get('no')

        # if not no: # validation
        #     return Response({'error': 'Bad request. phone number(no) is required'}, 
        #                         status=status.HTTP_400_BAD_REQUEST)
                                
        # try:
        #     model_instance = Phone.objects.get(no=no)
        # except Phone.DoesNotExist:
        #     return Response({'error': 'Bad request. phone no.(no) must be registered first'}, 
        #                         status=status.HTTP_400_BAD_REQUEST)

        # if model_instance.expire is None:
        #     return Response({'error': 'Bad request. phone has been already verified'},
        #                         status=status.HTTP_400_BAD_REQUEST)

        # if model_instance.v_code is not v_code:
        #     return Response({'error': 'Bad request. v_code was wrong'},
        #                         status=status.HTTP_400_BAD_REQUEST)

        # if model_instance.expire < datetime.now():
        #     return Response({'error': 'Bad request. code has been expired'},
        #                         status=status.HTTP_400_BAD_REQUEST)

        # model_instance.expire = None
        # model_instance.save()
        # return Response({'success': 'Phone has been verified successfully', 'data': model_instance.pics}, status=status.HTTP_200_OK)

def send_v_code(pre, no):
    v_code = (str(random.random()) + DEFAULT_V_CODE)[2:6]
    # send sms to +pre no here
    return v_code

def get_expire():
    time_change = timedelta(seconds=SIMPLECAPTCHA_DURATION)
    return timezone.localtime() + time_change

def create_phone(pre, no, is_mobile=True):
    v_code=send_v_code(pre, no)
    expire=get_expire()
    phones = Phone.objects.filter(expire__lt=timezone.localtime())
    
    if phones:
        pid = phones[0].id
        phones[0].delete()

        return Phone.objects.create(
                                id=pid,
                                pre=pre, 
                                No=no, 
                                v_code=v_code, 
                                expire=expire,
                                is_mobile=is_mobile
                                )
    
    return Phone.objects.create(
                        pre=pre, 
                        No=no, 
                        v_code=v_code, 
                        expire=expire,
                        is_mobile=is_mobile
                        )