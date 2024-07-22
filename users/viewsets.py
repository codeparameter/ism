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
        try:
            user = User.objects.get(username=request.data.get('username'))
            user.delete()
        except User.DoesNotExist:
            pass

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        create_user(
            username=request.data.get('username'), 
            password=request.data.get('password'),
            pre=request.data.get('pre'),
            no=request.data.get('no'),
            email=request.data.get('email')
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

def create_user(username, password, pre, no, email):
    phone = Phone.objects.filter(No=no, pre=pre)[0]
    expire = phone.expire
    expired_users = User.objects.filter(expire__lt=timezone.localtime())
    
    if expired_users:
        first_expired = expired_users[0]
        first_expired.username = username
        first_expired.password = password
        first_expired.phone = phone
        first_expired.email = email
        first_expired.expire = expire
        first_expired.activity = Activity.objects.get(status='Verifying')
        first_expired.last_login = None
        first_expired.is_staff = 0
        first_expired.is_superuser = 0
        first_expired.is_active = 1
        first_expired.save()

        return first_expired

    return User.objects.create(
            username=username,
            password=password,
            phone=phone,
            email=email,
            expire=expire
            )