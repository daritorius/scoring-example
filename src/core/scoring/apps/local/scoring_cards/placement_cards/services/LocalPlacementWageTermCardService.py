# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementWageTermCard


class LocalPlacementWageTermCardService(BaseService):
    model_instance = LocalPlacementWageTermCard