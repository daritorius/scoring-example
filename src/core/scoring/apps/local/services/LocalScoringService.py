# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.models import LocalScoring
from django.utils.translation import ugettext as _


class LocalScoringService(BaseService):
    model_instance = LocalScoring