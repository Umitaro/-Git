from django.db import models

# Create your models here.
class BorderModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.TextField(max_length=200) 