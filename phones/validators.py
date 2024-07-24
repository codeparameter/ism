from django.utils import timezone

from rest_framework import serializers
from .models import Phone
from .viewsets import create_phone, get_expire, send_v_code

def validate_starts_with9(pre, no):
    if pre == '98' and no[0] != '9':
        raise serializers.ValidationError("phone number must start with 9.")

def validate_unique_phone(phone):
    if phone.dependency:
        raise serializers.ValidationError("phone already exists.")

def validate_has_v_code(phone):
    now = timezone.localtime()
    if now <= phone.expire:
        time_left = phone.expire - now
        raise serializers.ValidationError(f"v_code has been sent. please wait for {time_left.seconds} seconds.")

def validate_not_expired_phone(phone):
    if phone.expire:
        validate_has_v_code(phone)
        phone.v_code = send_v_code(phone.pre, phone.No)
        phone.expire = get_expire()
        phone.save()

def validate_mobile_phone(pre, no):
    validate_starts_with9(pre, no)
    phones = Phone.objects.filter(No=no, pre=pre)

    if phones:
        phone = phones[0]
        validate_unique_phone(phone)
        validate_not_expired_phone(phone)
    else:
        create_phone(pre, no)
            