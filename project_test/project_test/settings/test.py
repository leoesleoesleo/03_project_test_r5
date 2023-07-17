# Standard Library
from os import environ
from decouple import config
from .base import *  # noqa

DEBUG = True
#ROOT_URLCONF = f'{SITE_NAME}.{SITE_NAME}.urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS  # noqa
