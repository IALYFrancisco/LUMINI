import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LUMINI.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Lecture sécurisée via os.environ.get (None si non défini)
username = os.environ.get("PLATEFORM_ADMIN_USERNAME")
email = os.environ.get("PLATEFORM_ADMIN_EMAIL")
password = os.environ.get("PLATEFORM_ADMIN_PASSWORD")

# Vérification : toutes les variables sont-elles présentes ?
if not all([username, email, password]):
    print("❌ Erreur : une ou plusieurs variables d'environnement sont manquantes.")
    print("Variables requises : DJANGO_ADMIN_USERNAME, DJANGO_ADMIN_EMAIL, DJANGO_ADMIN_PASSWORD")
else:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superutilisateur '{username}' créé.")
    else:
        print(f"ℹ️ Le superutilisateur '{username}' existe déjà.")
