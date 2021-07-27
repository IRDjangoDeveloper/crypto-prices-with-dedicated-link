from django.db import models

# Create your models here.
class CoinRequest(models.Model):
    coinPrice = models.FloatField()
    coinLink = models.CharField(max_length=500, unique=True)