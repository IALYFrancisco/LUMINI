from django.shortcuts import render, redirect
import requests
import os
from .forms import ContactMessageForm
from django.utils import timezone
import json

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
            email_api_url = os.getenv('EMAIL_API_ENDPOINT')
            headers = {
                "accept": "application/json",
                "api-key": os.getenv('EMAIL_API_KEY'),
                "content-type": "application/json"
            }
            payload = {
                "sender": {
                    "name": "LUMINI",
                    "email": "franciscoialy43@gmail.com"
                },
                "to": [
                    {
                        "email": "ialyfrancisco7@gmail.com",
                        "name": "IALY Francisco Raymond | Administrateur de LUMINI"
                    }
                ],
                "subject": request.POST.message_object,
                "htmlContent": "<html><body><h1>Bonjour !</h1><p>Ceci est un test avec Brevo API.</p></body></html>"
            }

            response = requests.post(email_api_url, headers=headers, data=json.dumps(payload))
            print("Status Code:", response.status_code)
            print("Réponse JSON:", response.json())

            return redirect('Contact')
    else:
        form = ContactMessageForm()
        return render(request, 'contact.html', { 'form': form })