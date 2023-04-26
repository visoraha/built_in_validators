
from django.db import models
from django.core import validators

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(6)])
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE,)
    name=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(8)])
    url=models.URLField()
    email=models.EmailField()
    mbno=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

# BUILT IN VALIDATORS
   #MaxLengthValidator()
   #MinLengthValidator()
   #RegexValidator()
   #MinvalueValidator()
   #MaxvalueValidator()