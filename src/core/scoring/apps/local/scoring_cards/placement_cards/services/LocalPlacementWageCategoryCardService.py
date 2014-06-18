# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementWageCategoryCard
from django.utils.translation import ugettext_lazy as _


class LocalPlacementWageCategoryCardService(BaseService):
    model_instance = LocalPlacementWageCategoryCard