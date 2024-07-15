from django.db import models
from cities.models import City
from mines.models import Material, Mine

class Color(models.Model):
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

statuses = (
    ('Available', 'available'),
    ('Ordered', 'ordered'),
    ('Sold', 'sold'), # can't order
)

class Availability(models.Model):
    status = models.CharField(max_length=50, choices=statuses)

class Block(models.Model):
    pics = models.JSONField(default=list, blank=True)
    vids = models.JSONField(default=list, blank=True)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    mtr = models.ForeignKey(Material, blank=True, on_delete=models.CASCADE)
    ct = models.ForeignKey(City, blank=True, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    code = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    availability = models.ForeignKey(Availability, default=1, blank=True, on_delete=models.CASCADE) # status
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def city(self):
        return self.ct.name

    @property
    def material(self):
        return self.mtr.name

    @property
    def mine_name(self):
        return self.mine.name

    @property
    def color_name(self):
        return self.color.name

    @property
    def schema_name(self):
        return self.schema.name

    @property
    def quality_grade(self):
        return self.quality.grade

    @property
    def availability_status(self):
        return self.availability.status

