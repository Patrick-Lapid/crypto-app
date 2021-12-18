from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5)
    currPrice = models.DecimalField(max_digits=10, decimal_places=2)
    mrktcap = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

