# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext_lazy as _


class OnlineScoringItemsPlainModels(BasePlainModel):
    fields = ['local_scoring', 'is_processed']