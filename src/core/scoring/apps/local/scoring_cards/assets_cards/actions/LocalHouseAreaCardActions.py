# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseAreaCardService import \
    LocalHouseAreaCardService
from django.utils.translation import ugettext as _


class LocalHouseAreaCardActions(BaseScoringCardActions):
    service = LocalHouseAreaCardService()