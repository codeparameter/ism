from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from phones.models import Phone

class User(AbstractUser):
    phone = models.ForeignKey(Phone, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Check if the password is already hashed
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
