from django.db import models
from users.models import User
from cities.models import City
from phones.models import Phone

class Material(models.Model):
    name = models.CharField(max_length=50)

statuses = (
    ('Verifying', 'verifying'),
    ('Active', 'active'),
    ('Suspended', 'suspended'),
    ('Closed', 'closed'),
    ('Baned', 'baned'),
)

class Activity(models.Model):
    status = models.CharField(max_length=50, choices=statuses)

class Mine(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    adr = models.TextField('Address')
    ph_no = models.ForeignKey(Phone, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, default=1, blank=True, on_delete=models.CASCADE)

class MineStaff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
