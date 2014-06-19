# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalAgeScorePlainModel
from core.scoring.apps.local.scoring_cards.age_cards.actions.AgeScoringCardActions import AgeScoringCardActions
from core.scoring.apps.local.scoring_cards.age_cards.plain_models import LocalAgeScoringCardPlainModel
from core.scoring.apps.local.services.LocalAgeScoreService import LocalAgeScoreService
from django.utils.translation import ugettext as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class AgeScoringModule(BaseScoringModule):
    age_service = LocalAgeScoreService()
    age_card_actions = AgeScoringCardActions()

    def calculate_score(self, data):
        score = self.age_card_actions.get_min_score()
        if hasattr(data, 'profile_birthday'):
            age = self.calculate_age(data)
            age = self.cards.max_scoring_age if age > self.age_card_actions.get_max_age() else age
            data = LocalAgeScoringCardPlainModel(key=int(age))
            score = self.age_card_actions.service.get_item(**data.__dict__).value
        data = LocalAgeScorePlainModel(total_score=score)
        age_data = self.age_service.create(data)
        return age_data

    def calculate_age(self, data):
        birthday = datetime.datetime.strptime(data.profile_birthday, BASE_DATE_FORMAT)
        return self._get_age(birthday)

    def _get_age(self, birthday):
        if birthday.month > datetime.date.today().month:
            age = datetime.date.today().year - birthday.year - self.age_card_actions.year_correction
        elif birthday.month == datetime.date.today().month:
            if birthday.day > datetime.date.today().day:
                age = datetime.date.today().year - birthday.year - self.age_card_actions.year_correction
            else:
                age = datetime.date.today().year - birthday.year
        else:
            age = datetime.date.today().year - birthday.year
        return age