from django.db import models

# Create your models here.

class CoffeeOriginCountry(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField('starting date of harvest')
    end_date = models.DateField('end date of harvest')
