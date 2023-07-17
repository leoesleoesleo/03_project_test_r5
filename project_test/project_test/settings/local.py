# Standard Library
from decouple import config
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS
