from django.contrib.auth.models import AbstractUser
from django.db import models
from phones.models import Phone

class User(AbstractUser):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
