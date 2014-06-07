# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.modules.AssetScoringModule import AssetScoringModule
from core.scoring.apps.local.actions.modules.CreditScoringModule import CreditScoringModule
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

    def generate_score(self, data):
        print '--------------------'
        age_score = self.age_scoring_module.calculate_score(data)
        print 'Age score: %s' % age_score
        print '--------------------'
        placement_score = self.placement_scoring_module.calculate_score(data)
        print 'Placement score: %s' % placement_score
        print '--------------------'
        personal_score = self.personal_scoring_module.calculate_score(data)
        print 'Personal score: %s' % personal_score
        print '--------------------'
        assets_score = self.asset_scoring_module.calculate_score(data)
        print 'Assets score: %s' % assets_score
        print '--------------------'
        loan_score = self.loan_scoring_module.calculate_score(data)
        print 'Loan score: %s' % loan_score
        print '--------------------'
        total_score = age_score + placement_score + personal_score + assets_score + loan_score
        print 'Total score: %s' % total_score
        print 'Total rating: "%s"' % self.calculate_rating(total_score)
        print '--------------------'
        return {'rating': self.calculate_rating(total_score), 'score': total_score}

    def calculate_rating(self, total_score):
        rating = 'G'
        for item in sorted(self.main_local_scoring_card.get_card(),
                           key=lambda key: self.main_local_scoring_card.get_card()[key]):
            if total_score < float(self.main_local_scoring_card.get_card()[item]):
                rating = item
                break
        return rating