from django.shortcuts import render, HttpResponse


def about_page(request):
    # return HttpResponse("This is the Bridges About Page")
    return render(request, 'about/index.html')


def our_team(request):
    return render(request, 'ourTeam/index.html')


def get_involved(request):
    return HttpResponse("This is the Bridges Get Involved Page")
