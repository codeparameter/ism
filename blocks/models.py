from django.db import models
from mines.models import Mine

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
    pics = models.JSONField(default=list, blank=True)
    vids = models.JSONField(default=list, blank=True)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    not_available = models.BooleanField(default=False, blank=True) # status
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

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
    def quality_name(self):
        return self.quality.grade

