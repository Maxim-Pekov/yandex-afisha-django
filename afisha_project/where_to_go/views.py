from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def show_place_id(place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_json = {
        "title": place.title,
        "imgs": [image.img.url for image in place.imgs.order_by('position').all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.coordinates_lng,
            "lat": place.coordinates_lat
        }
    }
    return JsonResponse(place_json, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def show_place(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinates_lng, place.coordinates_lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_json', args=[place.id])
            }
        },)
    places_geo = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'where_to_go/index.html', context={'places': places_geo})
