"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from os import *
import os
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'products',
    'Cars',
    'post',
    'profile_maker',
    'home',
    'registration',
    'subscribe',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# This URL is important as it will be the base URL for all static files of your project. This URL should be of the same name as the folder where your static file is stored.
STATIC_URL = '/static/'
# This setting contains the address of the folder where we will be storing static files. When we execute the collectstatic command, the Django will store our files in this directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'root')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'boot'),
    os.path.join(BASE_DIR, 'media'),
]  # This list has file-paths of the folders where we store our static files. When we execute the collectstatic command, Django will look for static files in these directories. Then it will save them in our STATIC_ROOT folder.


#  settings for file upload
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'profile_root')


#  MEDIA_ROOT is an empty string by default. It takes in the absolute file path of a directory. We have used the same join functions in Django static files tutorial that we have passed in the file path of media directory. This directory will store all the files a user uploads in Django.
#  EDIA_URL works the same way as STATIC_URL. This URL is used by Django instead of serving files with an absolute path. When Django will serve an uploaded file media it will be automatically added to the URL.
#  Note:
# MEDIA_URL & STATIC_URL should always have different values. Also, this goes for MEDIA_ROOT & STATIC_ROOT settings too. It was common in the past to use media root to all server static files. With the experiences of developers, this approach has some serious security implications.
# It is mandatory to have different values for media settings and static settings.


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# this is where you need to create your ENVIRON Variable
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# the EMAIL_USER and EMAIL_PASS are Enviro Variables holding sensitive info
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# to create enviro variables see below instructions
# 1. Install Django Environ - In your terminal, inside the project directory, type: pip install django-environ
# 2. Import environ in settings.py - import environ
# 3. Initialise environ - Below your import in settings.py:
""" import environ
# Initialise environment variables #
env = environ.Env()
environ.Env.read_env() """
# 4. Create your .env file - In the same directory as settings.py, create a file called ‘.env’
# 5. Declare your environment variables in .env - Make sure you don’t use quotations around strings.
# 6. IMPORTANT: Add your .env file to .gitignore
# 7. Replace all references to your environment variables in settings.py