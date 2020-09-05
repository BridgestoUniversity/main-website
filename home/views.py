from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("This is the Bridges Homepage")
