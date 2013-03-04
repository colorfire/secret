from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=50)
    come_from = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
