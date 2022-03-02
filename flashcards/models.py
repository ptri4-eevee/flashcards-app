from django.db import models

# Create your models here.
class Pattern(models.Model):
  #id is automatically added and autoincrements from 1
  question = models.CharField(max_length=1000, null=False)
  answer = models.CharField(max_length=1000, null=False)
  
  def __str__(self):
   return self.id
