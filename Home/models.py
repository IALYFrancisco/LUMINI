from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class ContactMessage(models.Model):
    client_name = models.CharField(max_length=40)
    client_phone = models.CharField(max_length=20)
    client_email = models.CharField(max_length=50)
    message_object = models.CharField()
    message = models.CharField()
    type = models.CharField()
    register_date = models.DateField("Date d'envoie")

    def __str__(self):
        return self.message
    
    def was_registered_recently(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)