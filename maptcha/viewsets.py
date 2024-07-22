# import time
# from datetime import timedelta
from django.utils import timezone
# from django.utils.encoding import smart_str
# from captcha.conf import settings as captcha_settings
from captcha.models import CaptchaStore#, randrange, MAX_RANDOM_KEY
from captcha.helpers import captcha_image_url

from rest_framework import status
from rest_framework.response import Response
from .models import *
from home.mixins import GetViewSet

class GetCaptchaViewSet(GetViewSet):
    permission_classes = ()

    def list(self, request, *args, **kwargs):

        CaptchaStore.objects.filter(expiration__lt=timezone.localtime()).delete()
        captcha_key = CaptchaStore.generate_key()

        return Response({'captcha_url': captcha_image_url(captcha_key)}, status=status.HTTP_200_OK)
