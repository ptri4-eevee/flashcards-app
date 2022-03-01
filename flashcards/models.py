from django.db import models

# Create your models here.
class PatternTable(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name

class Pattern(models.Model):
  #id is automatically added and autoincrements from 1
  table = models.ForeignKey(PatternTable, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=False)
  question = models.CharField(max_length=1000, null=False)
  answer = models.CharField(max_length=10000, null=False)
  def __str__(self):
    return self.name
