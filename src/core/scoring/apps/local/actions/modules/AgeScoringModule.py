# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalAgeScorePlainModel
from core.scoring.apps.local.scoring_cards.AgeScoringCard import AgeScoringCard
from core.scoring.apps.local.services.LocalAgeScoreService import LocalAgeScoreService
from django.utils.translation import ugettext as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class AgeScoringModule(BaseScoringModule):
    cards = AgeScoringCard()
    age_service = LocalAgeScoreService()

    def calculate_score(self, data):
        score = self.cards.min_age_score
        if hasattr(data, 'profile_birthday'):
            age = self.calculate_age(data)
            age = self.cards.max_scoring_age if age > self.cards.max_scoring_age else age
            score = self.cards.get_age_scoring_card()[str(age)]
        data = LocalAgeScorePlainModel(total_score=score)
        age_data = self.age_service.create(data)
        return age_data

    def calculate_age(self, data):
        birthday = datetime.datetime.strptime(data.profile_birthday, BASE_DATE_FORMAT)
        return self._get_age(birthday)

    def _get_age(self, birthday):
        if birthday.month > datetime.date.today().month:
            age = datetime.date.today().year - birthday.year - self.cards.year_correction
        elif birthday.month == datetime.date.today().month:
            if birthday.day > datetime.date.today().day:
                age = datetime.date.today().year - birthday.year - self.cards.year_correction
            else:
                age = datetime.date.today().year - birthday.year
        else:
            age = datetime.date.today().year - birthday.year
        return age