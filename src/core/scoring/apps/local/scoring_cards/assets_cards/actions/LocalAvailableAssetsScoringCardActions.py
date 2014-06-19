# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalAssetsScoringCardService import \
    LocalAssetsScoringCardService
from django.utils.translation import ugettext as _


class LocalAvailableAssetsScoringCardActions(BaseScoringCardActions):
    service = LocalAssetsScoringCardService()

    def get_card(self):
        return self.service.get_all()