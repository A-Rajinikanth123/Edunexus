import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edunexus.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
updated = User.objects.filter(is_active=False).update(is_active=True)
print(f"Activated {updated} users.")
