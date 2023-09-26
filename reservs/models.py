from django.db import models

# Create your models here.
class Reserv(models.Model):
    date = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    number_of_customers = models.CharField(max_length=200)