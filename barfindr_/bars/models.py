from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=200)
    locx = models.FloatField()
    locy = models.FloatField()
    address = models.CharField(max_length=300)
    hours_open = models.TimeField()
    hours_close = models.TimeField()
    hours_happy_start = models.TimeField()
    hours_happy_end = models.TimeField()

    def __str__(self):
    	return self.name

