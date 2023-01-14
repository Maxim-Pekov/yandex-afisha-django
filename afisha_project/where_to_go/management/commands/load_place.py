import requests, os

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from where_to_go.models import Place, Image


class Command(BaseCommand):
    help = 'Скачивает данные с GITHUB в базу проекта'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json_url',
            action='store',
            dest='json_url',
            type=str,
            default='',
            help='Введите url к json файлу с данными о локациях'
        )

    def write_imgs_to_db(self, place, img_urls):
        for img_url in img_urls:
            response = requests.get(img_url)
            response.raise_for_status()
            img_title = os.path.basename(img_url)
            content = ContentFile(response.content, img_title)
            Image.objects.get_or_create(
                place=place[0],
                img=content
            )

    def write_place_to_bd(self, place_details):
        coordinates = place_details['coordinates']
        place = Place.objects.get_or_create(
            title=place_details.get('title'),
            defaults={
                'description_short': place_details.get('description_short'),
                'description_long': place_details.get('description_long'),
                'lng': coordinates.get('lng'),
                'lat': coordinates.get('lat'),
            },
        )
        self.write_imgs_to_db(place, place_details.get('imgs'))

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        self.write_place_to_bd(response.json())
