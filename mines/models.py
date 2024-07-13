from django.db import models
from cities.models import City
from phones.models import Phone

class Material(models.Model):
    name = models.CharField(max_length=50)

class Mine(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    adr = models.TextField('Address')
    phone = models.OneToOneField(Phone, on_delete=models.CASCADE)

# role model
# users model