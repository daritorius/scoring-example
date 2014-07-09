#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings

apps = [
    ## user apps
    'core.users.user',
    'core.users.profile',
    'core.users.customers',

    ## scoring apps
    'core.scoring.apps.country',
    'core.scoring.apps.local',
    'core.scoring',

    ## scoring cards apps
    'core.scoring.apps.local.scoring_cards.age_cards',
    'core.scoring.apps.local.scoring_cards.assets_cards',
    'core.scoring.apps.local.scoring_cards.cities_cards',
    'core.scoring.apps.local.scoring_cards.loan_cards',
    'core.scoring.apps.local.scoring_cards.personal_cards',
    'core.scoring.apps.local.scoring_cards.placement_cards',

    ## online scoring apps
    'core.scoring.apps.online',
    'core.scoring.apps.online.apps.geo',
    'core.scoring.apps.online.apps.personal',
    'core.scoring.apps.online.apps.search_engines',
    'core.scoring.apps.online.apps.social_networks',

    ## report apps
    'core.main.reports'
]

for app_name in apps:
    if app_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (app_name,)