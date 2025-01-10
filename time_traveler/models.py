from django.db import models

# Create your models here.

class TimeTraveler(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10 , unique=True)
    gender = models.CharField(max_length=50)

    class Meta:
        db_table = 'time_traveler'