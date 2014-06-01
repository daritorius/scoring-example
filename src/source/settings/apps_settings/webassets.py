# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from .. import main_settings as settings


ASSETS_AUTO_BUILD = True
ASSETS_CACHE = True
ASSETS_ROOT = settings.STATIC_ROOT
ASSETS_URL = settings.STATIC_URL

ASSETS_DEFAULT_CSS_FILTERS = 'cssrewrite, cssmin'
ASSETS_DEFAULT_JS_FILTERS = 'rjsmin'