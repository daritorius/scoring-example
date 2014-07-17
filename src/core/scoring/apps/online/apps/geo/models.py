# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseGeoModel(BaseModel):
    query = models.TextField(max_length=65535, blank=True, null=True)
    data = models.TextField(max_length=65535, blank=True, null=True)

    class Meta:
        abstract = True


class GeoGoogle(BaseGeoModel):

    class Meta:
        db_table = 'geo_google_data'
        verbose_name = _(u'Geo Google Data')
        verbose_name_plural = _(u'Geo Google Data')


class GeoYandex(BaseGeoModel):

    class Meta:
        db_table = 'geo_yandex_data'
        verbose_name = _(u'Geo Yandex Data')
        verbose_name_plural = _(u'Geo Yandex Data')