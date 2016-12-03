import json
from django.shortcuts import render
from django.conf import settings
from .models import Location
from django.http import HttpResponse

def index(request):

    c = {"api_key": settings.MAPS_API_KEY}
    t = "stuff_map/index.html"

    return render(request, t, c)


def sample_json(request):

    # first get the home location
    home = Location.objects.get(home=True)

    # get the rest of the locations
    all_locations = Location.objects.exclude(pk=home.pk).order_by("id")

    locations = []
    for l in all_locations:
        locations.append(l.as_dict())

    # build the dictionary to return as json
    result = {
        "home": home.as_dict(),
        "locations": locations
    }

    return HttpResponse(json.dumps(result), content_type="application/json")
