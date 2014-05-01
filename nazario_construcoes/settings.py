# -*- coding: utf-8 -*-

"""
Django settings for nazario_construcoes project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '51^apct=zibmd%*!kj84h3*0w=7q1fu#nkj-ubq2^!@&5v0lt%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gerenciador_despesas',
    'gerenciador_contatos',
    'outros',
    'relatorios',
    'notificacoes',
    'south',
    'django_cron',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nazario_construcoes.urls'

WSGI_APPLICATION = 'nazario_construcoes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nazario_construcoes2',
        'USER': 'root',
        'PASSWORD': 'nazario4270'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    join(BASE_DIR, 'relatorios/templates')
)

STATICFILES_DIRS = (
    join(BASE_DIR, "static"),
)

SUIT_CONFIG = {
    # HEADER
    'ADMIN_NAME': 'Nazário Construções v2.0',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # FORMS
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    'MENU_OPEN_FIRST_CHILD': False,
    'MENU_EXCLUDE': ('django_cron',),
    'MENU': (
        {'app': 'auth',
         'label': 'Permissoes',
         'icon': 'icon-lock'},

        '-',

        {'app': 'gerenciador_despesas',
         'label': 'Gerenciador de Despesas',
         'icon': 'icon-shopping-cart'},

        {'app': 'gerenciador_contatos',
         'label': 'Gerenciador de Contatos',
         'icon': 'icon-user'},

        {'app': 'outros',
         'label': 'Outros',
         'icon': 'icon-tag'},
    )
}

CRON_CLASSES = [
    'notificacoes.cron_email.EnviarEmail',
]
