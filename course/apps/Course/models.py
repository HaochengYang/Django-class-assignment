from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coursenames(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Descriptions(models.Model):
    course= models.OneToOneField(Coursenames)
    decription = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
