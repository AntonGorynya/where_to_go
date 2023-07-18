from urllib.parse import urljoin
from where_to_go.settings import STATIC_URL, MEDIA_URL
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from .models import Place


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
                    'details': reverse('place-detail', args=(place.id,)),
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


def place_detail(request, place_id  ):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all()
    serialized_place = {
        'title': place.title,
        'imgs': [urljoin(MEDIA_URL, image.image.url) for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lon': place.lng,
        }
    }
    return JsonResponse(serialized_place, safe=True, json_dumps_params={'ensure_ascii': False, 'indent': 2})
