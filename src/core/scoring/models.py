# -*- coding: utf-8 -*-
import datetime
import random
import string
from core.main.base.BaseModel import BaseModel
from core.scoring.apps.local.models import LocalScoring
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Scoring(BaseModel):
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
    local_score = models.ForeignKey(LocalScoring, max_length=255, blank=True, null=True)
    user_data = models.TextField(max_length=65535, blank=True, null=True)
    # databases_check = models.BooleanField(default=False)
    # history_score = models.IntegerField(max_length=255, blank=True, null=True)
    # social_score = models.IntegerField(max_length=255, blank=True, null=True)
    # recommendation_score = models.IntegerField(max_length=255, blank=True, null=True)
    # psyho_score = models.IntegerField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        if not self.user_number:
            self.user_number = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(27))
        from core.scoring.services.ScoringService import ScoringService
        service = ScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'base_scoring'
        verbose_name = _(u'Base scoring')
        verbose_name_plural = _(u'Base scoring')