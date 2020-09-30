from django.shortcuts import render, HttpResponse


# def contact_page(request):
# return HttpResponse("This is the Bridges Contact Page")
# context = {'title': 'bridges', 'purpose': 'to help students'}
# return render(request, 'contact.html', context)
# return render(request, 'contact/bob.html')

def contactpage(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        return render(request, 'contact/index.html', {'name': name})

    else:
        return render(request, 'contact/index.html', {})
