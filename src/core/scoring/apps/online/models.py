# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


class OnlineScoringItems(BaseModel):
    local_scoring = models.ForeignKey('scoring.Scoring', blank=True, null=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'online_scoring_items'
        verbose_name = _(u'Online scoring items')
        verbose_name_plural = _(u'Online scoring items')