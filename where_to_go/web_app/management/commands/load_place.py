import os
import json
import zipfile
from django.core.management.base import BaseCommand
from ...models import Image, Place
import requests


PLACES_URL = 'https://github.com/devmanorg/where-to-go-places/archive/refs/heads/master.zip'
VERBOSE = True
TEMP_DIR = 'TMP'

class Command(BaseCommand):
    help = 'Наполнение БД тестовыми данными'

    def handle(self, *args, **kwargs):
        response = requests.get(PLACES_URL)
        response.raise_for_status()

        _, filename = os.path.split(PLACES_URL)
        os.makedirs(TEMP_DIR, exist_ok=True)
        filename = os.path.join(TEMP_DIR, filename)
        if VERBOSE:
            print(f'{filename} downloading...\nPlease wait.')
        with open(filename, 'wb') as file:
            file.write(response.content)
        if VERBOSE:
            print('download completed.\nUnzipping...')
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(TEMP_DIR)
        if VERBOSE:
            print('Unzipped.\nProcessing...')
        places_folder = os.path.join(TEMP_DIR, 'where-to-go-places-master', 'places')
        media_folder = os.path.join(TEMP_DIR, 'where-to-go-places-master', 'media')
        for place_file_name in os.listdir(places_folder):
            with open(os.path.join(places_folder, place_file_name), encoding='utf-8') as file:
                place_meta = json.load(file)
                place, created = Place.objects.get_or_create(
                    title=place_meta['title'],
                    lng=place_meta['coordinates']['lng'],
                    lat=place_meta['coordinates']['lat']
                )

                if created:
                    place.description_short = place_meta['description_short']
                    place.description_long = place_meta['description_long']
                    for order, imgs_meta in enumerate(place_meta['imgs']):
                        _, filename = os.path.split(imgs_meta)
                        image = Image.objects.create(
                            place=place,
                            order=order
                        )
                        with open(os.path.join(media_folder, filename), 'rb') as file:
                            image.image.save(filename, file, save=True)
                    place.save()

