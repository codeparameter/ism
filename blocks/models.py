from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)

class Material(models.Model):
    name = models.CharField(max_length=50)

class Schema(models.Model):
    name = models.CharField(max_length=50)

GRADES = (
    ('s+', 'S+'),
    ('s', 'S'),
    ('a+', 'A+'),
    ('a', 'A'),
    ('b+', 'B+'),
    ('b', 'B'),
    ('l', 'L'),
)

# class QualityManager(models.Manager):
#     def create_quality(self, grade):
#         quality = self.create(grade=grade)
#         return quality

class Quality(models.Model):
    grade = models.CharField(max_length=2, choices=GRADES)
    
    # objects = QualityManager()

class Block(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    available = models.BooleanField(default=True)

    @property
    def city_name(self):
        return self.city.name

    @property
    def material_name(self):
        return self.material.name

    @property
    def schema_name(self):
        return self.schema.name

    @property
    def Quality_name(self):
        return self.quality.grade
