# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.scoring_cards.AssetScoringCard import AssetScoringCard
from django.utils.translation import ugettext_lazy as _


class AssetScoringModule(BaseScoringModule):
    cards = AssetScoringCard()

    def calculate_score(self, data):
        available_assets_score = self.calculate_available_assets_score(data)
        print 'available assets score: %s' % available_assets_score
        total_assets_score = available_assets_score
        return total_assets_score

    def calculate_available_assets_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_assets, 'assets_available_assets'):
            score = self.cards.get_available_assets_card()[getattr(data.profile_assets, 'assets_available_assets')[0]]
        return score