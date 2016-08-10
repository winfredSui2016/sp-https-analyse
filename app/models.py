from django.db import models

# Create your models here.
from django.db import models


class resources(models.Model):
    ID = models.AutoField(primary_key=True)
    URL = models.CharField(max_length=2000)
    ParentURL = models.CharField(max_length=2000)
    ResourceType = models.CharField(max_length=255)
    Domain = models.CharField(max_length=2000)
    Type = models.CharField(max_length=255)
    IsHttps = models.CharField(max_length=4)
    Time = models.TimeField()