from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrkcap = models.DecimalField(max_digits=10, decimal_places=2)

