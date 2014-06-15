# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.models import Scoring
from django.utils.translation import ugettext as _


class ScoringService(BaseService):
    model_instance = Scoring