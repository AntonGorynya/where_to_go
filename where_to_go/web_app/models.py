from django.db import models
from django import forms

class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_short = models.TextField(default='Пару слов о месте', verbose_name='Краткое описание')
    description_long = models.TextField(default='Подробное описание места', verbose_name='Подробное Описание')
    placeId = models.CharField(max_length=50, verbose_name='placeId')
    #detailsUrl = models.CharField(max_length=50, verbose_name='detailsUrl')
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.title} {self.lon} {self.lat}'


class Image(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер')
    image = models.ImageField('Изображение', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['place', 'number'], name='name of constraint')
        ]

    def __str__(self):
        return f'{self.number} {self.place}'

    # @classmethod
    # def validate_number(cls, image):
    #     numbers = list(cls.objects.filter(place=image.place).values('number').distinct())
    #     numbers = [num['number'] for num in numbers]
    #     print(numbers)
    #     print(image.number)
    #     if image.number in numbers or image.number < 1:
    #         raise forms.ValidationError('Номера должны отличаться и быть положительны')

    # def clean(self):
    #     self.validate_number(self)
