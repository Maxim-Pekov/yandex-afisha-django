from django.db import models
from afisha_project import settings
from pathlib import Path
print(f'это путь ---->>> {Path(__file__)}')
# print(settings.MEDIA_ROOT / 'max')

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    coordinates_lng = models.FloatField('Долгота', blank=True, null=True)
    coordinates_lat = models.FloatField('Широта', blank=True)

    def __str__(self):
        return f'{self.title} {self.coordinates_lng} {self.coordinates_lat}'

    class Meta:
        ordering = ['title']
        verbose_name = 'Метка на карте'
        verbose_name_plural = 'Метки на карте'


class Image(models.Model):
    position = models.PositiveIntegerField()
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    img = models.ImageField(
        'Изображение',
        upload_to='images/%Y-%m-%d/'
    )
    places = models.ForeignKey(
        Place,
        related_name='imgs',
        verbose_name='Изображения',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def contact_default(self):
        return

