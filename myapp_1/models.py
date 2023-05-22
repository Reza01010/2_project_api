from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    R = [
        ('G', 'Gold'),
        ('s', 'silver'),
    ]
    Rating = models.CharField(max_length=10, choices=R, default='S')


class Cryptocurrency1(models.Model):
    name = models.CharField(max_length=200, blank=True)
    usd_price = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    datetime_moified = models.DateTimeField(auto_now=True)


class Cryptocurrency2(models.Model):
    response_data = models.JSONField(blank=True)
    datetime_moified = models.DateTimeField(auto_now=True)


class Cryptocurrency23(models.Model):
    response_datA = models.JSONField(blank=True)
    datetime_moified = models.DateTimeField(auto_now=True)

