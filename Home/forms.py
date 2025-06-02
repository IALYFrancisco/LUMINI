from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'client_name',
            'client_phone',
            'client_email',
            'message_object',
            'date_reason',
            'message'
        ]