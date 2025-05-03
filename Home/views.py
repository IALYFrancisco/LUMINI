from django.shortcuts import render
import requests
import os
# Create your views here.

def index(request):
    _headers = {
        'x-api-key' : os.getenv('PROJECT_API_KEY')
    }
    response = requests.get(f"{os.getenv('API_URL')}", headers=_headers)
    context = {
        "projects" : response.json()["data"]
    }
    return render(request, 'index.html', context)