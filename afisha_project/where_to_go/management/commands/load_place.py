import requests, os

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from where_to_go.models import Place, Image


class Command(BaseCommand):
    help = 'Скачивает данные с GITHUB в базу проекта'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--json_url',
            action='store',
            dest='json_url',
            type=str,
            default=0.0,
            help='Max value'
        )

    def write_json_to_bd(self, json):
        title = json['title']
        description_short = json['description_short']
        description_long = json['description_long']
        coordinates = json['coordinates']
        coordinates_lng = coordinates['lng']
        coordinates_lat = coordinates['lat']
        imgs = json['imgs']
        place = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            coordinates_lng=coordinates_lng,
            coordinates_lat=coordinates_lat
        )

        for count, img_url in enumerate(imgs):
            file = requests.get(img_url)
            img_name = os.path.basename(img_url)
            content = ContentFile(file.content, f'{img_name}')
            Image.objects.get_or_create(
                place=place[0],
                img=content
            )

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        print(response.json())
        self.write_json_to_bd(response.json())
