# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalOtherAssetsPriceCardService import \
    LocalOtherAssetsPriceCardService
from django.utils.translation import ugettext as _
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions


class LocalOtherAssetsPriceCardActions(BaseScoringCardActions):
    service = LocalOtherAssetsPriceCardService()