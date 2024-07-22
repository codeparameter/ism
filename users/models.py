from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from phones.models import Phone

statuses = (
    ('Verifying', 'verifying'),
    ('Active', 'active'),
    ('Suspended', 'suspended'),
    ('Baned', 'baned'),
)

class Activity(models.Model):
    status = models.CharField(max_length=50, choices=statuses)

class User(AbstractUser):
    phone = models.ForeignKey(Phone, null=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, default=1, blank=True, on_delete=models.CASCADE)
    expire = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the password is already hashed
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
