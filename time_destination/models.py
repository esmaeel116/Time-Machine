from django.db import models

# Create your models here.

class TimeDestination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    origin = models.CharField(max_length=1024)
    destination = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'time_destination'