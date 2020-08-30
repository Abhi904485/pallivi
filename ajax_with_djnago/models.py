from django.db import models


# Create your models here.
class listing_model(models.Model):
    title = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.title
