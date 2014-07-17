# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.main.base.BaseModel import BaseModel
from django.db import models


class BasePersonalData(BaseModel):
    query = models.CharField(max_length=1024, blank=True, null=True)
    data = models.TextField(max_length=65535, blank=True, null=True)

    class Meta:
        abstract = True


class WantedDetectData(BaseModel):

    def __unicode__(self):
        return u'ID: %s | query: %s | data: %s' % (self.id, self.query, self.data)

    class Meta:
        db_table = 'wanted_detect_data'
        verbose_name = _(u'Wanted person data')
        verbose_name_plural = _(u'Wanted persons data')


class MissedDetectData(BaseModel):

    def __unicode__(self):
        return u'ID: %s | query: %s | data: %s' % (self.id, self.query, self.data)

    class Meta:
        db_table = 'missed_detect_data'
        verbose_name = _(u'Missed person data')
        verbose_name_plural = _(u'Missed persons data')