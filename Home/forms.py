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

        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'ex: John Doe'}),
            'client_phone': forms.TextInput(attrs={'placeholder': 'ex: + 261 ... ... ...'}),
            'client_email': forms.EmailInput(attrs={'placeholder': 'ex: johndoe@example.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'Erivez votre message ...'}),
        }