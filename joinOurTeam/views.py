from django.shortcuts import render,HttpResponse

# Create your views here.
def joinOurTeam_page(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'joinOurTeam/index.html')