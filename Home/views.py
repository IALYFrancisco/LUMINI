from django.shortcuts import render, redirect
import requests
import os
from .forms import ContactMessageForm
from django.utils import timezone

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
        _form = ContactMessageForm(request.POST)
        if _form.is_valid():
            newContactMessage = _form.save(commit=False)
            if not newContactMessage.register_date:
                newContactMessage.register_date = timezone.now().date()
            newContactMessage.save()
            return redirect('Contact')
    else:
        form = ContactMessageForm()
        return render(request, 'contact.html', { 'form': form })