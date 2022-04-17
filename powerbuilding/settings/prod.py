import django_on_heroku                                                   # added to connect django and heroku 

from .base import *


SECRET_KEY = config('SECRET_KEY')


DEBUG = False   

ALLOWED_HOSTS = ['localhost', 'power-building.herokuapp.com']  




# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True