# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.country.models import Country
from django.utils.translation import ugettext_lazy as _


class CountryService(BaseService):
    model_instance = Country