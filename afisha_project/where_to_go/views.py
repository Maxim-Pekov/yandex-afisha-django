from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse


def show_place_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_json = {
        "title": place.title,
        "imgs": [ image.img.url for image in place.imgs.all() ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.coordinates_lng,
            "lat": place.coordinates_lat
        }
    }
    print(place_json)
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
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        },)
    places_geo = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'where_to_go/index.html', context={'places': places_geo})
