import os
from urllib.parse import urljoin
from where_to_go.settings import STATIC_URL, MEDIA_URL
from django.shortcuts import get_object_or_404
from django.shortcuts import render, loader
from django.http import HttpResponse, JsonResponse
from .models import Place, Image

def index(request):
    places = {
        'type': 'FeatureCollection',
        'features': []
    }
    for place in Place.objects.all():
        places['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(place.lon), float(place.lat)]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.placeId,
                    "detailsUrl": urljoin(STATIC_URL, place.detailsUrl),
                }
            }
        )
    context = {'places': places}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def place_detail(request, place_id=0):
    place = get_object_or_404(Place, pk=place_id)
    images = Image.objects.filter(place=place)
    place_meta = {
        'title': place.title,
        'imgs': [],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lon': place.lon,
        }
    }
    for image in images:
        place_meta['imgs'].append(urljoin(MEDIA_URL, str(image.name)))
    print(place_meta)
    return JsonResponse(place_meta, safe=True, json_dumps_params={'ensure_ascii': False})

