# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.models import LocalLoanScoring
from django.utils.translation import ugettext as _


class LocalLoanScoringService(BaseService):
    model_instance = LocalLoanScoring