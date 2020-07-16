"""
Django settings for restroomrater project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import random
import django_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('GAE_INSTANCE'):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['https://restroomrater.herokuapp.com/', '127.0.0.1']
# ALLOWED_HOSTS = ['*']
# if os.getenv('GAE_INSTANCE'):
#     ALLOWED_HOSTS = ['restroom-rater-281118.uc.r.appspot.com']
# else:
#     ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restroom_rater',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'restroomrater.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'restroom_rater.context_processors.search_form'
            ],
        },
    },
]

WSGI_APPLICATION = 'restroomrater.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

''' FOR LOCAL '''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

''' FOR DEPLOYED '''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'restrooms',
#         'USER': 'bathroom-user',
#         'PASSWORD': os.getenv('BATHROOM_PW'),
#         'HOST': '/cloudsql/restroom-rater-281118:us-central1:restroom-rater-db',
#         'PORT': '5432'
#     }
# }

# if not running at GAE, then replace the host with your local
# computer to connect to the database via cloud_sql_proxy
# if not os.getenv('GAE_INSTANCE'):
#     DATABASES['default']['HOST'] = '127.0.0.1'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

# Where in the file system to save user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if os.getenv('GAE_INSTANCE'):

    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_STATIC_FILE_BUCKET = 'restroom-rater-281118.appspot.com'
    STATIC_URL = f'https://storage.cloud.google.com/{GS_STATIC_FILE_BUCKET}/static/'

else:
    # for the site's static files
    STATIC_URL = '/static/'
    
    # Media URL, for user-created media - becomes part of URL when images are displayed
    MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'my_user_profile'
LOGOUT_REDIRECT_URL = 'homepage'

# Activate Django-Heroku.
django_heroku.settings(locals())

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)