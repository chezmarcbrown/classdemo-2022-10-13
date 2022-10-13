import re
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

from django.http import Http404

def flight(request, flight_id):
    try:
        f = Flight.objects.get(id = flight_id)
    except Flight.DoesNotExist:
        raise Http404("flight not found")
    return render(request, "flights/flight.html", {
        "flight": f,
        "passengers": f.passengers.all()
    })