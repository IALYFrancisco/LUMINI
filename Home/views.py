from django.shortcuts import render
import requests
import os
from .models import ContactMessage
from django.http import HttpResponse
# Create your views here.

def index(request):
    try:
        _headers = {
            'x-api-key' : os.getenv('PROJECT_API_KEY')
        }
        response = requests.get(f"{os.getenv('API_URL')}", headers=_headers)
        context = {
            "projects" : response.json()["data"]
        }
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            # newContactMessage = ContactMessage(request.POST)
            # newContactMessage.save()
            print(request.POST)
            return HttpResponse("Hello tpk.")
    else:
        return render(request, 'contact.html')