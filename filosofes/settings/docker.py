import os

from .base import *  # NOQA


ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', "pyarweb"),
        'USER': os.environ.get('DB_USER', "postgres"),
        'PASSWORD': os.environ.get('DB_PASS', ""),
        'HOST': os.environ.get('DB_SERVICE', "localhost"),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}
