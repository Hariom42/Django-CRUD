from django.db import models
from django.db.models.base import Model

# Create your models here.
class users (models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=60)
