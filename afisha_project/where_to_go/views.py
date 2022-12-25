from django.shortcuts import render
from .models import Place


def show_phones(request):
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
