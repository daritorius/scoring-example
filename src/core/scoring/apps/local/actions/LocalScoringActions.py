# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.BaseScoringActions import BaseScoringAction
from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule
from core.scoring.apps.local.actions.modules.PersonalScoringModule import PersonalScoringModule
from core.scoring.apps.local.actions.modules.PlacementScoringModule import PlacementScoringModule
from django.utils.translation import ugettext_lazy as _


class LocalScoringActions(BaseScoringAction):
    age_scoring_module = AgeScoringModule()
    placement_scoring_module = PlacementScoringModule()
    personal_scoring_module = PersonalScoringModule()

    def generate_score(self, data):
        age_score = self.age_scoring_module.calculate_score(data)
        print 'Age score: %s' % age_score
        placement_score = self.placement_scoring_module.calculate_score(data)
        print '\n'
        print '--------------------'
        print 'Placement score: %s' % placement_score
        personal_score = self.personal_scoring_module.calculate_score(data)
        print '--------------------'
        print 'Personal score: %s' % personal_score
        return 'A'