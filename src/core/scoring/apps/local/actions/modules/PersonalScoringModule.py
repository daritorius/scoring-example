# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.apps.local.plain_models import LocalPersonalScoringPlainModel
from core.scoring.apps.local.scoring_cards.cities_cards.actions.ScoringCityMillionaireActions import \
    ScoringCityMillionaireActions
from core.scoring.apps.local.scoring_cards.cities_cards.plain_models import ScoringCityMillionairePlainModel
from core.scoring.apps.local.scoring_cards.personal_cards.actions.LocalIdentityAddressesCardActions import \
    LocalIdentityAddressesCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.actions.LocalMaritalStatusBadCardActions import \
    LocalMaritalStatusBadCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.actions.LocalMaritalStatusNormalCardActions import \
    LocalMaritalStatusNormalCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.actions.LocalPersonalEducationCardActions import \
    LocalPersonalEducationCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.plain_models import LocalPersonalEducationCardPlainModel, \
    LocalMaritalStatusNormalCardPlainModel, LocalIdentityAddressesCardPlainModel
from core.scoring.apps.local.services.LocalPersonalScoringService import LocalPersonalScoringService
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule


class PersonalScoringModule(BaseScoringModule):
    min_normal_marital_age = 30
    max_normal_marital_age = 65
    personal_service = LocalPersonalScoringService()
    education_actions = LocalPersonalEducationCardActions()
    marital_status_normal_actions = LocalMaritalStatusNormalCardActions()
    marital_status_bad_actions = LocalMaritalStatusBadCardActions()
    identity_address_actions = LocalIdentityAddressesCardActions()
    millionaire_cities_actions = ScoringCityMillionaireActions()
    country_service = CountryService()

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
        score = self.education_actions.get_min_score()
        if hasattr(data.profile_personal_information, 'personal_education'):
            data = LocalPersonalEducationCardPlainModel(key=int(data.profile_personal_information.personal_education))
            score = self.education_actions.service.get_item(**data.__dict__).value if \
                self.education_actions.service.get_item(**data.__dict__) else self.education_actions.get_min_score()
        return score

    def calculate_marital_status_score(self, data):
        score = self.marital_status_bad_actions.get_min_score()
        if hasattr(data.profile_personal_information, 'personal_marital_status'):
            from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule

            age_module = AgeScoringModule()
            age = age_module.calculate_age(data)
            data = LocalMaritalStatusNormalCardPlainModel(
                key=int(data.profile_personal_information.personal_marital_status))
            if self.min_normal_marital_age <= age < self.max_normal_marital_age:
                score = self.marital_status_normal_actions.service.get_item(**data.__dict__).value if \
                    self.marital_status_normal_actions.service.get_item(**data.__dict__) else \
                    self.marital_status_normal_actions.get_min_score()
            else:
                score = self.marital_status_bad_actions.service.get_item(**data.__dict__).value if \
                    self.marital_status_bad_actions.service.get_item(**data.__dict__) else \
                    self.marital_status_bad_actions.get_min_score()
        return score

    def calculate_official_address_score(self, data):
        score = self.identity_address_actions.min_score
        if hasattr(data.profile_official_address, 'official_city'):
            data = ScoringCityMillionairePlainModel(
                country=self.country_service.get_item(title=data.country),
                title=getattr(data.profile_official_address, 'official_city').lower())
            if self.millionaire_cities_actions.service.get_item(**data.__dict__):
                score = self.identity_address_actions.max_score
        return score

    def calculate_real_address_score(self, data):
        score = self.identity_address_actions.min_score
        if hasattr(data.profile_official_address, 'real_city'):
            data = ScoringCityMillionairePlainModel(
                country=self.country_service.get_item(title=data.country),
                title=getattr(data.profile_official_address, 'real_city').lower())
            if self.millionaire_cities_actions.service.get_item(**data.__dict__):
                score = self.identity_address_actions.max_score
        return score

    def calculate_identity_real_official_address(self, data):
        score = self.identity_address_actions.get_min_score()
        if hasattr(data, 'profile_addresses_similar'):
            data = LocalIdentityAddressesCardPlainModel(key=int(getattr(data, 'profile_addresses_similar')))
            score = self.identity_address_actions.service.get_item(**data.__dict__).value if \
                self.identity_address_actions.service.get_item(**data.__dict__) else \
                self.identity_address_actions.get_min_score()
        return score