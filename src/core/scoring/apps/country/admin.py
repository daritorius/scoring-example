# -*- coding: utf-8 -*-
from core.scoring.apps.country.models import Country
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


admin.site.register(Country)