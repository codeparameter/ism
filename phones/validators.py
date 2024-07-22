from rest_framework import serializers

from .models import Phone

def validate_unique_phone(pre, no):
    phones = Phone.objects.filter(No=no, pre=pre)
    if phones:
        if phones[0].dependency:
            raise serializers.ValidationError("phone already exists.")

def validate_starts_with9(pre, no):
    if pre == '98' and no[0] != '9':
        raise serializers.ValidationError("phone number must start with 9.")

def validate_mobile_phone(pre, no):
    validate_unique_phone(pre, no)
    validate_starts_with9(pre, no)
            