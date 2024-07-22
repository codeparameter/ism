from django.utils import timezone

from rest_framework import serializers
from captcha.models import CaptchaStore
from .models import User


def validate_captcha(captcha_response):
    try:
        captcha = CaptchaStore.objects.get(response=captcha_response)
        captcha.delete()
    except CaptchaStore.DoesNotExist:
        raise serializers.ValidationError("captcha don't exist.")

def validate_phone_v_code(username, v_code):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise serializers.ValidationError("username don't exist.")

    if user.v_code != v_code:
        raise serializers.ValidationError("v_code dose't match.")

    if user.phone.expire:
        now = timezone.localtime()
        if now > user.phone.expire:
            raise serializers.ValidationError(f"v_code has been expired.")
            