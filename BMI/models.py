from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Patient(models.Model):
    Height = models.FloatField()
    Weight = models.FloatField()
    
    def bmi(self):
        return self.Weight / self.Height ** 2
    

'''
class BmiMeasurement(models.Model):
    HeightMeters = models.FloatField()
    WeightKilograms = models.FloatField()
    
    def bmi(self):
        return self.WeightKilograms / self.HeightMeters ** 2
'''
'''
#working
class Patient(models.Model):
    Height = models.CharField(max_length=200)
    Weight = models.CharField(max_length=200)

    def __str__(self):
        return self.Height + ' ' + self.Weight
'''