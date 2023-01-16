from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    description_short = models.TextField(
        'Короткое описание',
        blank=True
    )
    description_long = HTMLField(
        'Длинное описание',
        blank=True
    )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Метка на карте'
        verbose_name_plural = 'Метки на карте'


class Image(models.Model):
    position = models.PositiveIntegerField('Позиция', default=0)
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
