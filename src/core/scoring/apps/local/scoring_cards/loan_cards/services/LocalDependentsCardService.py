# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.loan_cards.models import LocalDependentsCard
from django.utils.translation import ugettext as _


class LocalDependentsCardService(BaseService):
    model_instance = LocalDependentsCard