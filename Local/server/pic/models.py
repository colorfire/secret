from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=50)
    herf = models.CharField(max_length=255)
    come_from = models.SlugField()
    local = models.FilePathField()
    create_date = models.DateTimeField(auto_now=True)
