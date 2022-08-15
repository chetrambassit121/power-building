"""
WSGI config for powerbuilding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

'''default'''
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings')    


'''Connecting wsgi to dev.py'''
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "powerbuilding.settings.dev"
)  


application = get_wsgi_application()
