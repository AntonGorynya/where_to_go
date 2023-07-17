import os
from urllib.parse import urljoin
from where_to_go.settings import STATIC_URL, MEDIA_URL
from django.shortcuts import get_object_or_404
from django.shortcuts import render, loader
from django.http import HttpResponse, JsonResponse
from .models import Place, Image


def index(request):
    features = []
    for place in Place.objects.all():
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(place.lng), float(place.lat)]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'details': f'places/{place.id}/',
                }
            }
        )
    context = {
        'places': {
            'type': 'FeatureCollection',
            'features': features
        }
    }
    return render(request, 'index.html', context=context)


def get_place_meta(place):
    images = place.images.all()
    place_meta = {
        'title': place.title,
        'imgs': [urljoin(MEDIA_URL, image.image.url) for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lon': place.lng,
        }
    }
    return place_meta


def place_detail(request, place_id=0):
    place = get_object_or_404(Place, pk=place_id)
    place_meta = get_place_meta(place)
    return JsonResponse(place_meta, safe=True, json_dumps_params={'ensure_ascii': False, 'indent': 2})
