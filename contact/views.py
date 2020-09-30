from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail


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

        # send an email
        send_mail(
            'Message from ' + name, # subject
            message, # message
            email, # from email
            ['bridgestouniversity@gmail.com'], # to email
        )

        return render(request, 'contact/index.html', {'name': name})

    else:
        return render(request, 'contact/index.html', {})
