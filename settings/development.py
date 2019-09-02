"""
Django development settings
"""
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wpd_@tlx_&wvsf27mjvh&+86mb^tytrmo37-$k3)uuag6hrrj%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce',
        'USER': 'ecom_admin',
        'PASSWORD': 'Admin2019',
        'HOST': 'localhost',
        'PORT': '',
    }
}