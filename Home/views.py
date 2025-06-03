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
                "subject": f"{_form.cleaned_data['message_object']}",
                "htmlContent": f"<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Document</title></head><body><main style=\"width: 100%;\"><section style=\"background-color: #073B4C; color: white; width: 100%; max-width: 600px; padding: 25px; margin: 100px auto; border-radius: 5px;\"><a href=\"https://lumini.onrender.com\" style=\"color: white;\"><h1 style=\"font-family: 'Trebuchet MS', Arial, sans-serif; display: flex; align-items: center;\"><img src=\"logo-de-LUMINI.png\" alt=\"Logo de LUMINI\" title=\"Logo de LUMINI\" style=\"width: 40px; margin-right: 5px;\">LUMINI</h1></a><h2 style=\"font-family: 'Trebuchet MS', Arial, sans-serif; margin-top: 50px;\">Bonjour IALY Francisco Raymond 😀,</h2><p style=\"margin-top: 20px; font-family: 'Trebuchet MS', Arial, sans-serif;\">{_form.cleaned_data['client_name']} vous a laissé un message sur LUMINI</p><a href=\"https://lumini.onrender.com\"><button  style=\"margin-top: 50px;color: #073B4C;font-size: 14px;font-weight: 500;background-color: white;border-style: solid;border-width: 2px;border-radius: 3px;border-color: #ffffff;cursor: pointer;padding: 8px 10px;\">aller sur LUMINI</button></a></section></main></body></html>"
            }

            response = requests.post(email_api_url, headers=headers, data=json.dumps(payload))
            print("Status Code:", response.status_code)
            print("Réponse JSON:", response.json())
            if _form.cleaned_data['message_object'] == 'simple':
                messages.success(request, f"Merci { _form.cleaned_data['client_name'] } 😊, le responsable recevra votre message et on vous répondra après, à bientôt 👋.")
            if _form.cleaned_data['message_object'] == 'date':
                messages.success(request, f"Merci { _form.cleaned_data['client_name'] } 😊, le responsable recevra votre message et on vous appellera après, à bientôt 👋.")

            return redirect('Contact')
    else:
        form = ContactMessageForm()
        return render(request, 'contact.html', { 'form': form })