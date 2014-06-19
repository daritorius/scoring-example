# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarStatusCardService import \
    LocalCarStatusCardService
from django.utils.translation import ugettext as _


class LocalCarStatusCardActions(BaseScoringCardActions):
    service = LocalCarStatusCardService()