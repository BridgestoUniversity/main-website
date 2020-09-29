from django.shortcuts import render, HttpResponse

from .models import Articles


def articles_page(request):
    # return HttpResponse("This is the Bridges Article Page")
    return render(request, 'articles/index.html')


def articles_testing(request, id):
    test = Articles.objects.get(id=id)
    return HttpResponse("<h1>Article Title: %s</h1><p>Date: %s</p><p>Topics: %s</p><p>Tags: %s</p><p>ArticleType: %s</p><p>Summary: %s</p><p>Authors: %s</p><p>Link: %s</p>" % (test.title, test.date, test.topics, test.tags, test.articleType, test.summary, test.authors, test.link))
