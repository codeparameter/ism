from django.db import models
from django.core.validators import MinLengthValidator


V_CODE_LENGTH = 4
DEFAULT_V_CODE = '0' * V_CODE_LENGTH

class Phone(models.Model):
    No = models.CharField('No', max_length=10, validators=[MinLengthValidator(10)])
    pre = models.CharField('pre', default='98', max_length=4, validators=[MinLengthValidator(1)])
    # pre + no uniqueness must validate together
    is_mobile = models.BooleanField(default=True, blank=True)
    dependency = models.JSONField(default=dict, blank=True) # type content
    expire = models.DateTimeField(null=True, blank=True)
    v_code = models.CharField('v_code', default=DEFAULT_V_CODE, max_length=V_CODE_LENGTH, validators=[MinLengthValidator(V_CODE_LENGTH)]) # verification code
