from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from first_app.models import Contact
from django.core.mail import send_mail
from . import models
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        newContact = models.Contact(name = name,
                               email = email,
                               message = message)

        newContact.save()
        send_gmail(name,email,message)
        # subject = 'Contact Form Received'
        # from_email = settings.DEFAULT_FROM_EMAIL
        # to_email = [settings.

    return HttpResponseRedirect('/')

def send_gmail(name,email,message):
    send_mail(
        'New enquiry',
        'Name: '+name+'\nEmail: '+email+'\nMessage: '+message,
        'server@vanillaarcade.com',
        ['server@vanillaarcade.com'],
        fail_silently=False,
    )

def newsletter_subscription(request):
    if request.method == "POST":
        email = request.POST.get("email")
        newSubscription = models.Newsletter(email = email)
        # print(email)
        # obj = models.Newsletter.objects.get(email=email)
        # print(obj)
        # if obj is None and obj == '':
        #     print("ASSHOLE")
        #     newSubscription.save()
        newSubscription.save()

    return HttpResponseRedirect('/')

def website_logo(request):
    img = models.WebsiteLogo.objects.all().last()    #For the most recent image in db
    return render_to_response("first_app/index.html", {"img": img})
    # newImage = models.WebsiteLogo.objects.all()[:1].get()
    # newImage = models.WebsiteLogo.objects.all().order_by('-id')
