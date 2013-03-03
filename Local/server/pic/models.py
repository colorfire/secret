from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=50)
    herf = models.SlugField()
    come_from = models.CharField(max_length=255)
    local = models.FilePathField(blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
