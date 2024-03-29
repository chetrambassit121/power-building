import os  
from pathlib import Path

import dj_database_url  
import django_on_heroku  
# from decouple import (
#     config,
# )  
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = (
    Path(__file__).resolve().parent.parent.parent
)  


'''Application definition'''
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "powerbuilding_information",
    "members",
    "social",
    "lists",
    # "fitness",

    # third party 
    "django_extensions",
    "crispy_forms",  
    "ckeditor",  
    "ckeditor_uploader",  
    "rest_framework",
    "whitenoise.runserver_nostatic",
    "debug_toolbar",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
]

ROOT_URLCONF = "powerbuilding.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "powerbuilding.wsgi.application"

AUTH_USER_MODEL = "members.User"  

''' added for cripsy forms its also accessing bootstrap4 '''
CRISPY_TEMPLATE_PACK = (
    "bootstrap4"  
)


''' for ckeditor and django ckeditor 5 '''
DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

'''Only who upload image see it '''
CKEDITOR_RESTRICT_BY_USER = True   
CKEDITOR_UPLOAD_PATH = "uploads/"

'''Shows directory of image in the server'''
CKEDITOR_BROWSE_SHOW_DIRS = True 

'''Arranges image in terms of date uploaded'''
CKEDITOR_RESTRICT_BY_DATE = True  
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {"toolbar": None, "extraPlugins": "codesnippet",},
}


'''
   Database
   https://docs.djangoproject.com/en/3.2/ref/settings/#databases
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


'''
    required for the dj_databse_url module
    https://pypi.org/project/django-database-url/
'''
db_from_env = dj_database_url.config(
    conn_max_age=500
)  
DATABASES["default"].update(
    db_from_env
)  


'''
    Password validation
    https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
'''
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


'''
    Internationalization
    https://docs.djangoproject.com/en/3.2/topics/i18n/
'''
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


'''media files'''
MEDIA_URL = "/media/"  
MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)  


''' 
    Static files (CSS, JavaScript, Images)
    https://docs.djangoproject.com/en/3.2/howto/static-files/
'''
STATIC_URL = "/static/"  
STATICFILES_DIRS = [  
    os.path.join(
        BASE_DIR, "static"
    ),  
]
STATIC_ROOT = os.path.join(
    BASE_DIR, "staticfiles"
)  
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  


'''
    login and logout returns user to homepage
    https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
'''
LOGIN_REDIRECT_URL = "home"  
LOGOUT_REDIRECT_URL = "home"  


'''email hidden variables'''
EMAIL_BACKEND = str(os.getenv("EMAIL_BACKEND"))
EMAIL_USE_TLS = str(os.getenv("EMAIL_USE_TLS"))
EMAIL_HOST = str(os.getenv("EMAIL_HOST"))
EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER"))
DEFAULT_FROM_EMAIL = str(os.getenv("DEFAULT_FROM_EMAIL"))
EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))
EMAIL_PORT = str(os.getenv("EMAIL_PORT"))



'''
    Default primary key field type
    https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
'''
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',   # added from DRF JWT
        # 'rest_framework.authentication.BasicAuthentication'
    ],
    "DEFAULT_PERMISSIONS_CLASSES": [
        # 'rest_framework.permissions.AllowAny',
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

'''required for django heroku'''
django_on_heroku.settings(locals())  
