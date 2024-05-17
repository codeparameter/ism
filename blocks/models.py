from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)

class Material(models.Model):
    name = models.CharField(max_length=50)

class Schema(models.Model):
    name = models.CharField(max_length=50)

class Quality(models.Model):
    grade = models.CharField(max_length=50)

class Block(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    material = models.ForeignKey("Material", on_delete=models.CASCADE)
    schema = models.ForeignKey("Schema", on_delete=models.CASCADE)
    quality = models.ForeignKey("Quality", on_delete=models.CASCADE)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    available = models.BooleanField(default=True)
