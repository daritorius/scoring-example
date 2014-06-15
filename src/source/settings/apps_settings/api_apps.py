#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings

apps = [
    'api',
]

for app_name in apps:
    if app_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (app_name,)