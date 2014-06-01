#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings

apps = [
    'core.users.user',
    'core.users.profile',

    ## scoring apps
    'core.scoring.apps.country',
    'core.scoring',
    'core.scoring.apps.local',
]

for app_name in apps:
    if app_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (app_name,)