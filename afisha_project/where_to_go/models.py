from django.db import models
from afisha_project import settings
from pathlib import Path
print(f'это путь ---->>> {Path(__file__)}')
print(settings.MEDIA_ROOT / 'max')

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    coordinates_lng = models.FloatField('Долгота', blank=True, null=True)
    coordinates_lat = models.FloatField('Широта', blank=True)

    def __str__(self):
        return f'{self.title} {self.coordinates_lng} {self.coordinates_lat}'


class Image(models.Model):
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
    position = models.PositiveIntegerField()


