from django.db import models
from django.core.validators import MinLengthValidator


class Phone(models.Model):
    No = models.CharField('No', unique=True, max_length=10, validators=[MinLengthValidator(10)])
    pre = models.CharField('pre', default='98', max_length=4, validators=[MinLengthValidator(1)]) 
    is_mobile = models.BooleanField(default=True, blank=True)
    dependency = models.JSONField(default=list, blank=True)
