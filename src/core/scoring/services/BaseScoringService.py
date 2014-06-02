# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.models import BaseScoring
from django.utils.translation import ugettext as _


class BaseScoringService(BaseService):
    model_instance = BaseScoring