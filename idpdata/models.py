from django.db import models

# Create your models here.
class User(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    age = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    needs = models.CharField(max_length=370)
