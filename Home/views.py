from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import ContactMessageForm
import requests
import os
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
                "subject": "Object Message",
                "htmlContent": "<html><body><h1>Bonjour !</h1><p>Ceci est un test avec Brevo API.</p></body></html>"
            }

            # response = requests.post(email_api_url, headers=headers, data=json.dumps(payload))
            # print("Status Code:", response.status_code)
            # print("Réponse JSON:", response.json())

            messages.success(request, "Merci users_name 😊, le responsable recevra votre message et on vous répondra après, à bientôt 👋.")

            return redirect('Contact')
    else:
        form = ContactMessageForm()
        return render(request, 'contact.html', { 'form': form })