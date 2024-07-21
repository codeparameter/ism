from rest_framework import serializers

from .models import Activity, User
from home.validators import validate_int
from phones.validators import validate_mobile_phone

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'id',
            'status',
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

class UserRegistrationSerializer(serializers.ModelSerializer):
    pre = serializers.CharField(validators=[validate_int], max_length=4)
    no = serializers.CharField(validators=[validate_int], max_length=10, min_length=10)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'pre',
            'no',
        )
        
    def validate(self, attrs):
        validate_mobile_phone(pre=attrs['pre'], no=attrs['no'])
        return super().validate(attrs)
