from rest_framework import serializers
from captcha.models import CaptchaStore


def validate_captcha(captcha_response):
    try:
        CaptchaStore.objects.get(response=captcha_response)
    except CaptchaStore.DoesNotExist:
        raise serializers.ValidationError("captcha don't exist.")
            