# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementTypeCard
from django.utils.translation import ugettext as _


class LocalPlacementTypeCardService(BaseService):
    model_instance = LocalPlacementTypeCard