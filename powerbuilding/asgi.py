"""
ASGI config for powerbuilding project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings')     # default
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerbuilding.settings.dev')   # edited above line ... added .dev so it will default to our powerbuilding/settings/dev.py


application = get_asgi_application()
