"""
WSGI config for powerbuilding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings')     # default
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings.dev')   # edited above line ... added .dev so it will default to our powerbuilding/settings/dev.py


application = get_wsgi_application()
