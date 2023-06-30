import os
from urllib.parse import urljoin
from where_to_go.settings import STATIC_URL
from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Place

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
