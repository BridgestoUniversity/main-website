from django.shortcuts import render, HttpResponse


def linktree_page(request):
    return render(request, 'linktree/index.html')
