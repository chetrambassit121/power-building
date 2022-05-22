"""
Django settings for powerbuilding project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os                                                              # added  ... os include many functions to interact with the file system.
                                                                       # https://www.geeksforgeeks.org/os-module-python-examples/



import dj_database_url                                                 # added ... This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
                                                                       # https://pypi.org/project/django-database-url/
from decouple import config                                            # added ... Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.
                                                                       # https://pypi.org/project/python-decouple/ 
import django_on_heroku                                                 # added to connect django and heroku 
   
from dotenv import load_dotenv
load_dotenv()    




# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent                    # original default code in this file
BASE_DIR = Path(__file__).resolve().parent.parent.parent               # when we created settings folder and moved settings.py into it ..
                                                                       # we need to add another parent since its within another folder





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_extensions',               # added 
    'powerbuilding_information',       # added this app we created 
    'members',                         # added this app we created 
    'social',                         # added this app we created 
    'crispy_forms',                    # added this app we downloaded ... this helps with any forms we want to create like login form, register form ... etc 
                                       # https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms 
    'ckeditor',                        # added this app we downloaded ... will help upload photos more easily
                                       # https://pytutorial.com/django-ckeditor
    # 'django_ckeditor_5',               # added this version of ck editior as well 
                                       # https://pypi.org/project/django-ckeditor-5/
    'ckeditor_uploader',               # added this since we downloaded ckeditor this is required for app to work 
    'rest_framework',
    "whitenoise.runserver_nostatic",
    # 'django-nose'
    'lists'
]





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware', # added ... to help serve static files during production follow this link https://medium.com/@naufal.ihsan21/how-to-serve-static-files-in-django-using-whitenoise-cda11f9bb643 
]

ROOT_URLCONF = 'powerbuilding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],                                                        # original default code
        'DIRS': [os.path.join(BASE_DIR, 'templates')],                       # added our own path for templates 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'powerbuilding.wsgi.application'

AUTH_USER_MODEL = 'members.User'                                                   # added "Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting that references a custom model:"


CRISPY_TEMPLATE_PACK = 'bootstrap4' # added for cripsy forms its also accessing bootstrap4


# # Use nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# # Tell nose to measure coverage on the 'foo' and 'bar' apps
# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=foo,bar',
# ]



# added for ckeditor and django ckeditor 5 
DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True #Only who upload image see it
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True # Shows directory of image in the server
CKEDITOR_RESTRICT_BY_DATE = True # Arranges image in terms of date uploaded
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': 'codesnippet',
    },
}
##############################




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


db_from_env = dj_database_url.config(conn_max_age=500)            # added ... required for the dj_databse_url module
DATABASES['default'].update(db_from_env)                          # added ... required for the dj_databse_url module
                                                                  # https://pypi.org/project/django-database-url/


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'                                            # added ... created a media folder which will store our users images, videos, etc                       
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')                     # added the path ... so media is for users , static is for the coder who wants to uplaod images, videos, etc
                                                                 # go to base directory (powerbuilding) access media folder 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'                                                           # url prefix that we will use to call upon the static files 

STATICFILES_DIRS = [                                                              # added .. tells django where to look for static files besides in the apps 
    os.path.join(BASE_DIR, 'static'),                                             # we want django to look inside our static folder that we created 
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')                                # added this root for the staticfiles .. during production all static files are collected and dumped into staticfiles folder
                                                                                   # using the command .. python manage.py collectstatic .. will take all static files and create then dump them into staticfiles folder 
                                                                                   # go to base directory (powerbuilding) access staticfiles folder 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'    # added for Adding compression and caching support


                                                                                     # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
LOGIN_REDIRECT_URL = 'home'                                                        # added will redirect to home page after logging in            
LOGOUT_REDIRECT_URL = 'home'                                                       # added will redirect to home page aftr logging out 


# added all email information which connects to the information in .env file .. we do not want our sensative information displayed here rather its displayed in hidden .env file
# EMAIL_BACKEND = config('EMAIL_BACKEND') 
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_BACKEND=config('EMAIL_BACKEND')
# EMAIL_USE_TLS=config('EMAIL_USE_TLS')
# EMAIL_HOST=config('EMAIL_HOST')
# EMAIL_HOST_USER=config('EMAIL_HOST_USER')
# DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL')
# EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT=config('EMAIL_PORT') 

# EMAIL_BACKEND=os.environ.get('EMAIL_BACKEND')
# EMAIL_USE_TLS=os.environ.get('EMAIL_USE_TLS')
# EMAIL_HOST=os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
# DEFAULT_FROM_EMAIL=os.environ.get('DEFAULT_FROM_EMAIL')
# EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_PORT=os.environ.get('EMAIL_PORT') 


EMAIL_BACKEND=str(os.getenv('EMAIL_BACKEND'))
EMAIL_USE_TLS=str(os.getenv('EMAIL_USE_TLS'))
EMAIL_HOST=str(os.getenv('EMAIL_HOST'))
EMAIL_HOST_USER=str(os.getenv('EMAIL_HOST_USER'))
DEFAULT_FROM_EMAIL=str(os.getenv('DEFAULT_FROM_EMAIL'))
EMAIL_HOST_PASSWORD=str(os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_PORT=str(os.getenv('EMAIL_PORT'))


# EMAIL_BACKEND = config('EMAIL_BACKEND')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = config('EMAIL_PORT')

# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# # DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# EMAIL_PORT = config('EMAIL_PORT')
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# EMAIL_HOST=os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS=os.getenv('EMAIL_USE_TLS')
# EMAIL_PORT=os.getenv('EMAIL_PORT')

###########################################



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',   # added from DRF JWT
        # 'rest_framework.authentication.BasicAuthentication'
    ],

    "DEFAULT_PERMISSIONS_CLASSES": [
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]

}

django_on_heroku.settings(locals())    # added ... required for django heroku 


