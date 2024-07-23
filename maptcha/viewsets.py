from django.utils import timezone
from captcha.conf import settings as captcha_settings
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from rest_framework import status
from rest_framework.response import Response
from .models import *
from home.mixins import GetViewSet

class GetCaptchaViewSet(GetViewSet):
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        challenge, response = captcha_settings.get_challenge(None)()
        expired_captchas = CaptchaStore.objects.filter(expiration__lt=timezone.localtime())
        if expired_captchas:
            cid = expired_captchas[0].id
            expired_captchas[0].delete()
            captcha = CaptchaStore.objects.create(id=cid, challenge=challenge, response=response)
        else:
            captcha = CaptchaStore.objects.create(challenge=challenge, response=response)
            
        return Response({'captcha_url': captcha_image_url(captcha.hashkey)}, status=status.HTTP_200_OK)
