# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseScoring(models.Model):
    user_number = models.CharField(db_index=True, max_length=255, blank=True, null=True)
    country = models.ForeignKey('country.Country', blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    local_score = models.IntegerField(max_length=255, blank=True, null=True)
    history_score = models.IntegerField(max_length=255, blank=True, null=True)
    databases_score = models.IntegerField(max_length=255, blank=True, null=True)
    social_score = models.IntegerField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        db_table = 'base_scoring'
        verbose_name = _(u'Base scoring')
        verbose_name_plural = _(u'Base scoring')