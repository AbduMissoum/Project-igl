"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent









SIMPLE_JWT = {
    # Set the access token to last 1 week
    'ACCESS_TOKEN_LIFETIME': timedelta(weeks=1),
    
    # Optionally, adjust the refresh token as well (e.g., 2 weeks)
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=2),

    # Keep other settings as default or customize as needed
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'SIGNING_KEY': 'your_secret_key_here',
    'ALGORITHM': 'HS256',
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8spne5qdl*e(omlj@81d$u1#0iwr88k)qu-%#ki7#06!=6stz1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'drf_spectacular',

    'drf_yasg',
    'rest_framework',
    'dpi',
    'bilan_bio',
    'authentication',
    'ordonnance.apps.OrdonnanceConfig',
    'consultation',
    'bilan_radio',
    'les_soins',
    'rest_framework.authtoken',
    'corsheaders',
  

]



# mailing service
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Ajoute ceci en haut de la liste
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'



SWAGGER_SETTINGS = {
   'DEFAULT_INFO': 'import.path.to.urls.api_info',
}
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

WSGI_APPLICATION = 'api.wsgi.application'
AUTH_USER_MODEL = 'authentication.CustomUser'
# settings.py





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mediumclone_igl5',
        'USER': '367579_abdallah',
        'PASSWORD': 'abdallah',
        'HOST': 'mysql-mediumclone.alwaysdata.net',  # Or your MySQL server's IP/hostname
        'PORT': '3306',  # Default MySQL port
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

SPECTACULAR_SETTINGS = {
    'TITLE': 'Soins API',
    'DESCRIPTION': 'API documentation for managing soins data.',
    'VERSION': '1.0.0',

    # This is typically not needed unless you have custom info.
    'DEFAULT_INFO': 'drf_spectacular.openapi.Info',  # Use the default info
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
         'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # Token-based auth
        'rest_framework.authentication.SessionAuthentication',  # Session-based auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Default permission
    ],
}
MEDIA_URL = '/media/'  # URL prefix for accessing media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directory on the server where files will be stored

CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',  # Ajoute l'URL de ton frontend Angular ici
]
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-requested-with',
    'accept',
    'origin',
    'accept-encoding',
    'x-csrftoken',
]

CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:4200',  # Add your frontend's URL here
    'https://localhost:4200',  # If you use HTTPS in local dev, also add this
        'http://localhost:4201',  # Add your frontend's URL here

]
# settings.py

# Enable CORS for all domains (for development)

# Or, allow only specific domains
# CORS_ALLOWED_ORIGINS = [
#     'http://yourfrontend.com',
# ]

# Allow all methods (including OPTIONS for preflight)


# Allow specific headers, if needed, like CSRF token and others

# Handle preflight request cache time
