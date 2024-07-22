# from rest_framework import serializers

# from .models import Activity, User
# from .validators import validate_phone_v_code
# from home.validators import validate_int
# from phones.validators import validate_mobile_phone
# from phones.models import V_CODE_LENGTH

# class ActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Activity
#         fields = (
#             'id',
#             'status',
#         )

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#         )

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     pre = serializers.CharField(validators=[validate_int], max_length=4)
#     no = serializers.CharField(validators=[validate_int], max_length=10, min_length=10)

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password',
#             'pre',
#             'no',
#             'email',
#         )
        
#     def validate(self, attrs):
#         validate_mobile_phone(pre=attrs['pre'], no=attrs['no'])
#         return super().validate(attrs)

# class UserPhoneVerificationSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=150)
#     v_code = serializers.CharField(validators=[validate_int], max_length=V_CODE_LENGTH, min_length=V_CODE_LENGTH)

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'v_code',
#         )
        
#     def validate(self, attrs):
#         validate_phone_v_code(attrs['username'], attrs['v_code'])
#         return super().validate(attrs)
