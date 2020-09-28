from django.shortcuts import render, HttpResponse


def articles_page(request):
    # return HttpResponse("This is the Bridges Article Page")
    return render(request, 'articles.html')
