# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeTermCardService import \
    LocalPlacementPeTermCardService
from django.utils.translation import ugettext_lazy as _


class LocalPlacementPeTermCardActions(BaseScoringCardActions):
    service = LocalPlacementPeTermCardService()