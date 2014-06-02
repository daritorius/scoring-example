# -*- coding: utf-8 -*-
import datetime
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

    user_number = models.CharField(db_index=True, max_length=255, blank=True, null=True)
    country = models.ForeignKey('country.Country', blank=True, null=True)
    rating = models.CharField(choices=GRADES, default=GRADE_G, max_length=255, blank=True, null=True)
    databases_check = models.BooleanField(blank=True, null=True, default=False)
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

    class Meta:
        db_table = 'base_scoring'
        verbose_name = _(u'Base scoring')
        verbose_name_plural = _(u'Base scoring')