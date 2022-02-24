from django.db import models

# Create your models here.
class MyPatterns(models.Model):
  #id is automatically added and autoincrements from 1
  name = models.CharField(max_length=100, null=False)
  question = models.CharField(max_length=1000, null=False)
  answer = models.CharField(max_length=10000, null=False)
