import requests
import logging

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.core.files.base import ContentFile
from where_to_go.models import Place, Image


logger = logging.getLogger(__name__)


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
        for count, img_url in enumerate(img_urls):
            response = requests.get(img_url)
            response.raise_for_status()
            img_title = f'image {count}'
            content = ContentFile(response.content, img_title)
            Image.objects.update_or_create(
                place=place,
                img=content,
                position=count
            )

    def write_place_to_bd(self, place_details):
        coordinates = place_details['coordinates']
        place, place_not_created = Place.objects.get_or_create(
            title=place_details['title'],
            defaults={
                'description_short': place_details.get(
                    'description_short', ''
                ),
                'description_long': place_details.get('description_long', ''),
                'lng': coordinates['lng'],
                'lat': coordinates['lat'],
            },
        )
        if place_not_created:
            self.write_imgs_to_db(place, place_details.get('imgs', []))

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        try:
            self.write_place_to_bd(response.json())
        except KeyError:
            logger.warning("Введите обязательные поля, title, lng, lat")