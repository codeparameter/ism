from django.db import models
from django.core.validators import MinLengthValidator


class Phone(models.Model):
    No = models.CharField('No', unique=True, max_length=11, validators=[MinLengthValidator(11)])