from .base import *

SECRET_KEY = str(os.getenv("SECRET_KEY"))


DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "localhost:8000",
    "power-building.herokuapp.com",
    "power-building.herokuapp.com/admin",
    "127.0.0.1",
]


'''HTTPS settings'''
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

'''HSTS settings'''
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
