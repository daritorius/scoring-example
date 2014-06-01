#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings

apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
]

for app_name in apps:
    if app_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (app_name,)