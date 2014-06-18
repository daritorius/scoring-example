# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementCleanIncomeCard
from django.utils.translation import ugettext_lazy as _


class LocalPlacementCleanIncomeCardService(BaseService):
    model_instance = LocalPlacementCleanIncomeCard