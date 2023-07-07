from django.db import models
from django import forms

class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_short = models.TextField(default='Пару слов о месте', verbose_name='Краткое описание')
    description_long = models.TextField(default='Подробное описание места', verbose_name='Подробное Описание')
    placeId = models.CharField(max_length=50, verbose_name='placeId')
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} {self.lon} {self.lat}'


class Image(models.Model):
    order = models.PositiveIntegerField(verbose_name='Порядковый номер', default=0)
    image = models.ImageField('Изображение', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place')

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(fields=['place', 'order'], name='name of constraint')
        # ]
        ordering = ['order', 'place']

    def __str__(self):
        return f'{self.order} {self.place}'

    # @classmethod
    # def validate_number(cls, image):
    #     numbers = list(cls.objects.filter(place=image.place).values('number').distinct())
    #     numbers = [num['number'] for num in numbers]
    #     print(numbers)
    #     print(image.number)
    #     if image.number in numbers:
    #         raise forms.ValidationError('Номера должны отличаться')

    # def clean(self):
    #     self.validate_number(self)
