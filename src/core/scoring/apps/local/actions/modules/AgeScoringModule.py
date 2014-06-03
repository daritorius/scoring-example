# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.scoring_cards.age_scoring_card import AGE_SCORING_CARD
from django.utils.translation import ugettext as _


class AgeScoringModule(BaseScoringModule):
    card = AGE_SCORING_CARD
    max_scoring_age = 75
    year_correction = 1
    min_age_score = -200

    def calculate_score(self, data):
        score = self.min_age_score
        if hasattr(data, 'profile_birthday'):
            age = self.calculate_age(data)
            age = self.max_scoring_age if age > self.max_scoring_age else age
            score = self.card[str(age)]
        return score

    def calculate_age(self, data):
        birthday = datetime.datetime.strptime(data.profile_birthday[0], "%d-%m-%Y")
        if birthday.month > datetime.date.today().month:
            age = datetime.date.today().year - birthday.year - self.year_correction
        elif birthday.month == datetime.date.today().month:
            if birthday.day > datetime.date.today().day:
                age = datetime.date.today().year - birthday.year - self.year_correction
            else:
                age = datetime.date.today().year - birthday.year
        else:
            age = datetime.date.today().year - birthday.year
        return age