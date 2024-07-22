from datetime import timedelta
from django.utils import timezone
import random

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import DEFAULT_V_CODE
from phones.viewsets import create_phone
from home.settings import SIMPLECAPTCHA_DURATION


class UserRegistrationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = User.objects.none()
    serializer_class = UserRegistrationSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        pre = request.data.get('pre')
        no = request.data.get('no')
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        v_code = send_v_code(pre, no)
        expire = get_expire()

        phone = create_phone(pre, no, expire)
        
        User.objects.create(
            username=request.data.get('username'), 
            password=request.data.get('password'),
            phone=phone,
            v_code=v_code,
            expire=expire
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        

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

        # if model_instance.v_code is not v_code:
        #     return Response({'error': 'Bad request. v_code was wrong'},
        #                         status=status.HTTP_400_BAD_REQUEST)

        # if model_instance.expire < datetime.now():
        #     return Response({'error': 'Bad request. code has been expired'},
        #                         status=status.HTTP_400_BAD_REQUEST)

def send_v_code(pre, no):
    v_code = int((str(random.random()) + DEFAULT_V_CODE)[2:6])
    # send sms to +pre no here
    return v_code

def get_expire():
    time_change = timedelta(seconds=SIMPLECAPTCHA_DURATION)
    return timezone.localtime() + time_change