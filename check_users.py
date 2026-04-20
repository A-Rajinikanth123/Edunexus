import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edunexus.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
for u in User.objects.all():
    print(f"Username: {u.username}, Email: {u.email}, Active: {u.is_active}, Role: {u.role}")
