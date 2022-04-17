from .base import *

SECRET_KEY = 'abc123'
# SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = True                                                                                 
ALLOWED_HOSTS = ['*']  # set to all hosts allowed 

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False