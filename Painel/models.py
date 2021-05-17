from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class DataInfo(models.Model):
    confirmedCases = models.IntegerField(default=0, verbose_name='confirmedCases')
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    country = models.OneToOneField(Country, on_delete=models.CASCADE, blank=True, unique=True)


# Create your models here.
