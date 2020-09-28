from django.shortcuts import render, HttpResponse


def homepage(request):
    # return HttpResponse("This is the Bridges Homepage")
    return render(request, 'home/index.html')
