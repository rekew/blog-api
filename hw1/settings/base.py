from pathlib import Path
from .conf import *
<<<<<<< HEAD
from datetime import timedelta
import os
=======
>>>>>>> 006ac0f38acdf1843bb88b1b22489f0a4a6405c8

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # PROJECT APPS
    'apps.users',
    'apps.blogs',

    # rest
    'rest_framework'
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "%(levelname)s - %(message)s",
        },
        "verbose": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(module)s | %(message)s",
        },
    },

    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },

        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "formatter": "verbose",
            "filename": os.path.join(BASE_DIR, "logs/app.log"),
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 3,
        },

        "debug_requests": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "verbose",
            "filename": os.path.join(BASE_DIR, "logs/debug_requests.log"),
            "filters": ["require_debug_true"],
        },
    },

    "loggers": {

        "users": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },

        "blogs": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },

        "django.request": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },

        "django.server": {
            "handlers": ["debug_requests"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

AUTH_USER_MODEL = 'users.User'
<<<<<<< HEAD
=======

# noqa
>>>>>>> 006ac0f38acdf1843bb88b1b22489f0a4a6405c8
