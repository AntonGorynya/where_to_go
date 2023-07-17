from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description_short = models.TextField(default='', verbose_name='Краткое описание')
    description_long = HTMLField(default='', verbose_name='Подробное Описание')
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    lat = models.DecimalField(max_digits=17, decimal_places=14)

    class Meta:
        ordering = ['title']
        unique_together = [['title', 'lng', 'lat']]

    def __str__(self):
        return f'{self.title} {self.lng} {self.lat}'


class Image(models.Model):
    order = models.PositiveIntegerField(verbose_name='Порядковый номер', default=0)
    image = models.ImageField('Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['order', 'place']

    def __str__(self):
        return f'{self.order} {self.place}'
