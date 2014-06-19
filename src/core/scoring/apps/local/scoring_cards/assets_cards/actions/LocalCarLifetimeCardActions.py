# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarLifetimeService import LocalCarLifetimeService
from django.utils.translation import ugettext as _


class LocalCarLifetimeCardActions(BaseScoringCardActions):
    service = LocalCarLifetimeService()