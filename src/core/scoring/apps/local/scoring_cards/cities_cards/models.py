# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from core.scoring.apps.country.models import Country
from django.db import models
from django.utils.translation import ugettext as _


class ScoringCityMillionaire(BaseModel):
    country = models.ForeignKey(Country, blank=True, null=True)
    title = models.CharField(_(u'Название'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        db_table = 'scoring_cities_millionaires'
        verbose_name = _(u'City millionaire')
        verbose_name_plural = _(u'City millionaires')