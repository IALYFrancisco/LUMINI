from django.db import models

# Create your models here.

class ContactMessage(models.Model):

    OBJECT_CHOICES = [
        ('simple', 'Simple prise de contact 🤝'),
        ('date', 'Prise de rendez-vous 📅'),
    ]

    DATE_REASON_CHOICES = [
        ('web', 'Création de site web | application web 🌐'),
        ('mobile', 'Création d\'application mobile 📱'),
        ('hosting', 'Mise en ligne d\'une application web | mobile 🧱')
    ]

    client_name = models.CharField(max_length=40, verbose_name="Votre nom :")
    client_phone = models.CharField(max_length=20, verbose_name="Votre numéro téléphone :")
    client_email = models.CharField(max_length=50, verbose_name="Votre email :")
    message_object = models.CharField(max_length=6, choices=OBJECT_CHOICES, default='web', verbose_name="Objet du contact :")
    message = models.TextField(verbose_name="Votre message :")
    date_reason = models.CharField(max_length=7, choices=DATE_REASON_CHOICES, default='simple', verbose_name="Raison du prise de rendez-vous :")
    register_date = models.DateField("Date d'envoie", auto_now_add=True)

    def __str__(self):
        return self.message