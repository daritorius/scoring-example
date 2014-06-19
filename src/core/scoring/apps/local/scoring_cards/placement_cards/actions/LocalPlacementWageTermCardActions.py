# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageTermCardService import \
    LocalPlacementWageTermCardService
from django.utils.translation import ugettext_lazy as _


class LocalPlacementWageTermCardActions(BaseScoringCardActions):
    service = LocalPlacementWageTermCardService()