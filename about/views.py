from django.shortcuts import render, HttpResponse

def about_page(request):
    return HttpResponse("This is the Bridges About Page")

def our_team(request):
    return HttpResponse("This is the Bridges Team Intro Page")