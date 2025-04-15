"""
Django settings for django_graphql project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'apps.book',
    # third party apps
    'graphene_django',
    # 'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'rest_framework',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': '5432',
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASS"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
#             "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
#             "region_name": os.getenv("S3_REGION"),  # e.g., "us-east-1"
#             "bucket_name": os.getenv("BUCKET_NAME")
#         },
#     },
#     "staticfiles": {  # For static files
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
#             "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
#             "region_name": os.getenv("S3_REGION"), # e.g., "us-east-1"
#             "bucket_name": os.getenv("BUCKET_NAME"),
#             "location": "static",  # Specify a folder within your bucket
#             "default_acl":"public-read"
#         },
#     },
# }

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DEFAULT_FILE_STORAGE = "config.settings.storages.default"  # Replace "config.settings" with your actual settings path
STATICFILES_STORAGE = "config.settings.storages.staticfiles"

GRAPHENE = {
    'SCHEMA': 'apps.book.graphql.schema',
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}
GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": timedelta(days=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=15),

}
