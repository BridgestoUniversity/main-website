from django.shortcuts import render,HttpResponse

# Create your views here.
def mentorship_page(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'mentorship/index.html')