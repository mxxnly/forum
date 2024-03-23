import os
from django.db import models
from django.conf import settings

class YourModel(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    link = models.URLField(max_length=200, default='')
    photo = models.ImageField(upload_to='', default='OIP.jpg')
    
    