# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext_lazy as _


class GeoGooglePlainModel(BasePlainModel):
    fields = ['query', 'data']


class GeoYandexPlainModel(BasePlainModel):
    fields = ['query', 'data']