# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.online.apps.geo.models import GeoYandex
from django.utils.translation import ugettext_lazy as _


class GeoYandexService(BaseService):
    model_instance = GeoYandex