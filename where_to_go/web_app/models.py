from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    placeId = models.CharField(max_length=50, verbose_name='placeId')
    detailsUrl = models.CharField(max_length=50, verbose_name='detailsUrl')
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.title} {self.lon} {self.lat}'
