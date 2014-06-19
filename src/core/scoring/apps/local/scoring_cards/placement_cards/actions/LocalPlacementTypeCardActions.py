# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementTypeCardService import \
    LocalPlacementTypeCardService
from django.utils.translation import ugettext as _


class LocalPlacementTypeCardActions(BaseScoringCardActions):
    service = LocalPlacementTypeCardService()