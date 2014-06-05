# -*- coding: utf-8 -*-
import datetime
import random
import string
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseScoring(models.Model):
    GRADE_A = 'A'
    GRADE_B = 'B'
    GRADE_C = 'C'
    GRADE_D = 'D'
    GRADE_E = 'E'
    GRADE_F = 'F'
    GRADE_G = 'G'

    GRADES = (
        (GRADE_A, 'A'),
        (GRADE_B, 'B'),
        (GRADE_C, 'C'),
        (GRADE_D, 'D'),
        (GRADE_E, 'E'),
        (GRADE_F, 'F'),
        (GRADE_G, 'G'),
    )

    user_number = models.CharField(db_index=True, unique=True, max_length=255, blank=True, null=True)
    country = models.ForeignKey('country.Country', blank=True, null=True)
    rating = models.CharField(choices=GRADES, default=GRADE_G, max_length=255, blank=True, null=True)
    databases_check = models.BooleanField(default=False)
    local_score = models.IntegerField(max_length=255, blank=True, null=True)
    history_score = models.IntegerField(max_length=255, blank=True, null=True)
    social_score = models.IntegerField(max_length=255, blank=True, null=True)
    recommendation_score = models.IntegerField(max_length=255, blank=True, null=True)
    psyho_score = models.IntegerField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        self.code = self.code.lower()
        self.title = self.title.lower()
        if not self.key:
            self.key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(27))
        from core.scoring.services.BaseScoringService import BaseScoringService
        service = BaseScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'base_scoring'
        verbose_name = _(u'Base scoring')
        verbose_name_plural = _(u'Base scoring')