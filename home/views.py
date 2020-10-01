from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Event


def homepage(request):
    # return HttpResponse("This is the Bridges Homepage")

    events = Event.objects
    eventsLatestOrder = events.order_by('date')

    eventsList = eventsLatestOrder

    return render(request, 'home/recents.html', {"events": eventsList})
