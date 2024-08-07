from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from .serializers import *
from phones.viewsets import Phone
from home.mixins import PostViewSet


class UserRegistrationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):
    serializer_class = UserRegistrationSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):        
        expired_user = User.objects.filter(username=request.data.get('username'), 
                                            expire__lt=timezone.localtime())
        if expired_user:
            uid = expired_user[0].id
            expired_user.delete()
        else:
            uid = None


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        create_user(
            username=request.data.get('username'), 
            password=request.data.get('password'),
            pre=request.data.get('pre'),
            no=request.data.get('no'),
            email=request.data.get('email'),
            uid=uid
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserPhoneVerificationViewSet(PostViewSet):
    serializer_class = UserPhoneVerificationSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(username=request.data.get('username'))
        user.expire = None
        user.phone.expire = None

        content_type = ContentType.objects.get_for_model(User)
        user.phone.dependency = {'content_type_id': content_type.id, 'instance_id': user.id}
        
        user.phone.save()
        user.save()

        return Response({'msg': 'phone verified'}, status=status.HTTP_200_OK)

def create_user(username, password, pre, no, email, uid=None):
    phone = Phone.objects.filter(No=no, pre=pre)[0]
    expire = phone.expire
    
    if uid:
        return User.objects.create(
                id=uid,
                username=username,
                password=password,
                phone=phone,
                email=email,
                expire=expire
                )

    expired_users = User.objects.filter(expire__lt=timezone.localtime())

    if expired_users:
        uid = expired_users[0].id
        expired_users[0].delete()

        return User.objects.create(
                id=uid,
                username=username,
                password=password,
                phone=phone,
                email=email,
                expire=expire
                )    

    return User.objects.create(
            username=username,
            password=password,
            phone=phone,
            email=email,
            expire=expire
            )