# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from django.db import models
from django.utils.translation import ugettext as _


class BaseScoringCardModel(BaseModel):
    key = models.IntegerField(_(u'Значение'), max_length=255, blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    class Meta:
        abstract = True
        ordering = ['value']