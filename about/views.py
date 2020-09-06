from django.shortcuts import render, HttpResponse

def about_page(request):
    return HttpResponse("This is the Bridges About Page")
