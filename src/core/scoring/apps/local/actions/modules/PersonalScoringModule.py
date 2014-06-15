# -*- coding: utf-8 -*-
from core.scoring.apps.local.plain_models import LocalPersonalScoringPlainModel
from core.scoring.apps.local.scoring_cards.CountryMillionCityCards import CountryMillionCityCards
from core.scoring.apps.local.scoring_cards.PersonalInformationCards import PersonalInformationCards
from core.scoring.apps.local.services.LocalPersonalScoringService import LocalPersonalScoringService
from django.utils.translation import ugettext as _
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule


class PersonalScoringModule(BaseScoringModule):
    cards = PersonalInformationCards()
    city_card = CountryMillionCityCards()
    personal_service = LocalPersonalScoringService()

    def calculate_score(self, data):
        education_score = self.calculate_education_score(data)
        print 'education score: %s' % education_score
        marital_status_score = self.calculate_marital_status_score(data)
        print 'maritial status score: %s' % marital_status_score
        official_address_score = self.calculate_official_address_score(data)
        print 'official address score: %s' % official_address_score
        real_address_score = self.calculate_real_address_score(data)
        print 'real address score: %s' % real_address_score
        identity_addresses_score = self.calculate_identity_real_official_address(data)
        print 'identity addresses score: %s' % identity_addresses_score
        total_score = education_score + \
                      marital_status_score + \
                      official_address_score + \
                      real_address_score + \
                      identity_addresses_score
        data = LocalPersonalScoringPlainModel(
            education_score=education_score,
            marital_status_score=marital_status_score,
            official_address_score=official_address_score,
            real_address_score=real_address_score,
            identity_addresses_score=identity_addresses_score,
            total_score=total_score,
        )
        personal_data = self.personal_service.create(data)
        return personal_data

    def calculate_education_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_personal_information, 'personal_education'):
            score = self.cards.get_education_card()[str(data.profile_personal_information.personal_education)]
        return score

    def calculate_marital_status_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_personal_information, 'personal_marital_status'):
            score = self.cards.get_marital_status_card()[str(data.profile_personal_information.personal_marital_status)]
        return score

    def calculate_official_address_score(self, data):
        score = self.cards.min_address_city_score
        if hasattr(data.profile_official_address, 'official_city'):
            if getattr(data.profile_official_address, 'official_city').lower() \
                    in self.city_card.get_millions_city_by_country(getattr(data, 'country')):
                score = self.cards.max_address_city_score
        return score

    def calculate_real_address_score(self, data):
        score = self.cards.min_address_city_score
        if hasattr(data.profile_real_address, 'real_city'):
            if getattr(data.profile_real_address, 'real_city').lower() \
                    in self.city_card.get_millions_city_by_country(getattr(data, 'country')):
                score = self.cards.max_address_city_score
        return score

    def calculate_identity_real_official_address(self, data):
        score = self.cards.min_identity_address_score
        if hasattr(data, 'profile_addresses_similar'):
            score = self.cards.get_identity_addresses_card()[str(getattr(data, 'profile_addresses_similar'))]
        return score