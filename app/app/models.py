from django.db import models

# Create your models here.

class CCTV(models.Model):
    Longitude = models.FloatField()
    Latitude = models.FloatField()
    Url = models.URLField()
    Description = models.CharField(max_length=50)

class LAMP(models.Model):
    Walt = models.IntegerField(null=True)
    X = models.FloatField()
    Y = models.FloatField()

class ACCIDENT(models.Model):
    Id = models.CharField(max_length=20, primary_key=True)
    Date = models.DateField()
    X = models.FloatField()
    Y = models.FloatField()
    Casualties = models.IntegerField()
    Type = models.CharField(max_length=50, null=True)

class SIDEWALK(models.Model):
    name = models.CharField(max_length=30)
    start_point = models.CharField(max_length=30)
    end_point = models.CharField(max_length=30)
    length = models.FloatField()
    width = models.FloatField()
    area = models.CharField(max_length=3)

class SIDEWALK_POINT(models.Model):
    Sidewalk = models.ForeignKey(SIDEWALK, on_delete=models.CASCADE, related_name='points')
    X = models.FloatField()
    Y = models.FloatField()
