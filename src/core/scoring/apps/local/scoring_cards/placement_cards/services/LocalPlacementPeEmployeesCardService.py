# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementPeEmployeesCard
from django.utils.translation import ugettext_lazy as _


class LocalPlacementPeEmployeesCardService(BaseService):
    model_instance = LocalPlacementPeEmployeesCard