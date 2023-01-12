from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    description_short = models.TextField('Короткое описание', blank=True, null=True)
    description_long = HTMLField('Длинное описание', blank=True, null=True)
    coordinates_lng = models.FloatField('Долгота', blank=True, null=True)
    coordinates_lat = models.FloatField('Широта', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Метка на карте'
        verbose_name_plural = 'Метки на карте'


class Image(models.Model):
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    img = models.ImageField(
        'Изображение',
        upload_to='images/%Y-%m-%d/'
    )
    place = models.ForeignKey(
        Place,
        related_name='imgs',
        verbose_name='Место на карте',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
