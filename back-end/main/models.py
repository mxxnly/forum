from django.db import models

# Create your models here.
class YourModel(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(upload_to='uploaded/')