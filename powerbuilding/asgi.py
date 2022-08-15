import os

from django.core.asgi import get_asgi_application

'''default connection'''
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings')

'''Connecting asgi to dev.py'''
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "powerbuilding.settings.dev"
) 

application = get_asgi_application()
