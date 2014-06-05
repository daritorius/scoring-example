# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext_lazy as _


class ScoringPlainModel(BasePlainModel):
    fields = ['user_number', 'country', 'rating', 'local_score']