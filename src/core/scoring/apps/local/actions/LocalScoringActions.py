# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.modules.AssetScoringModule import AssetScoringModule
from core.scoring.apps.local.actions.modules.CreditScoringModule import CreditScoringModule
from core.scoring.apps.local.plain_models import LocalScoringPlainModel
from core.scoring.apps.local.services.LocalScoringService import LocalScoringService
from core.scoring.scoring_cards.MainLocalScoringCard import MainLocalScoringCard
from django.utils.translation import ugettext_lazy as _
from core.scoring.apps.local.actions.BaseScoringActions import BaseScoringAction
from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule
from core.scoring.apps.local.actions.modules.PersonalScoringModule import PersonalScoringModule
from core.scoring.apps.local.actions.modules.PlacementScoringModule import PlacementScoringModule


class LocalScoringActions(BaseScoringAction):
    main_local_scoring_card = MainLocalScoringCard()
    age_scoring_module = AgeScoringModule()
    placement_scoring_module = PlacementScoringModule()
    personal_scoring_module = PersonalScoringModule()
    asset_scoring_module = AssetScoringModule()
    loan_scoring_module = CreditScoringModule()
    local_scoring_service = LocalScoringService()

    def generate_score(self, data):
        print '--------------------'
        age_score = self.age_scoring_module.calculate_score(data)
        print 'Age score: %s' % age_score.total_score
        print '--------------------'
        placement_score = self.placement_scoring_module.calculate_score(data)
        print 'Placement score: %s' % placement_score.total_score
        print '--------------------'
        personal_score = self.personal_scoring_module.calculate_score(data)
        print 'Personal score: %s' % personal_score.total_score
        print '--------------------'
        assets_score = self.asset_scoring_module.calculate_score(data)
        print 'Assets score: %s' % assets_score.total_score
        print '--------------------'
        loan_score = self.loan_scoring_module.calculate_score(data)
        print 'Loan score: %s' % loan_score.total_score
        print '--------------------'
        total_score = age_score.total_score + \
                      placement_score.total_score + \
                      personal_score.total_score + \
                      assets_score.total_score + \
                      loan_score.total_score
        print 'Total score: %s' % total_score
        print 'Total rating: "%s"' % self.calculate_rating(total_score)
        print '--------------------'
        data = LocalScoringPlainModel(
            age_score=age_score,
            placement_score=placement_score,
            personal_score=personal_score,
            assets_score=assets_score,
            loan_score=loan_score,
            total_score=total_score,
            rating=self.calculate_rating(total_score),
        )
        local_scoring_data = self.local_scoring_service.create(data)
        return local_scoring_data

    def calculate_rating(self, total_score):
        rating = 'G'
        for item in sorted(self.main_local_scoring_card.get_card(),
                           key=lambda key: self.main_local_scoring_card.get_card()[key]):
            if total_score >= self.main_local_scoring_card.max_score:
                rating = self.main_local_scoring_card.max_rate
            if total_score < int(self.main_local_scoring_card.get_card()[item]):
                rating = item
                break
        return rating