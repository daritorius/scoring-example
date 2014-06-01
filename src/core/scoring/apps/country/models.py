# -*- coding: utf-8 -*-
import datetime
import random
import string
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, unique=True)
    code = models.CharField(max_length=255, blank=True, null=True, db_index=True, unique=True)
    key = models.CharField(max_length=255, blank=True, null=True, unique=True)
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'ID: %s | title: %s | code: %s' % (self.id, self.title, self.code)

    def save(self, *args, **kwargs):
        if self.code:
            self.code = self.code.lower()
        if not self.key:
            self.key = ''.join(random.choice(string.lowercase + string.digits) for i in range(17))
        from core.scoring.apps.country.services.CountryService import CountryService
        service = CountryService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'countries'
        verbose_name = _(u'Country')
        verbose_name_plural = _(u'Countries')