from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def show_place_id(request, place_id):
    # place_id = request.params
    place = get_object_or_404(Place, pk=place_id)
    return HttpResponse(place.title)


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
