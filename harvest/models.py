from django.db import models


class CoffeeOriginCountry(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField("starting date of harvest")
    end_date = models.DateField("end date of harvest")
