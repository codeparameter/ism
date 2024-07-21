from rest_framework import serializers

from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    pre = serializers.CharField(max_length=4)
    no = serializers.CharField(max_length=10, min_length=10)
    class Meta:
        model = Phone
        fields = (
            'id',
            'pre',
            'No',
        )
