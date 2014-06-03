# -*- coding: utf-8 -*-
from api.facades.BaseScoringFacade import BaseScoringFacade
from core.main.base.facades.BaseFacade import BaseFacade
from core.scoring.apps.local.actions.LocalScoringActions import LocalScoringActions
from core.scoring.apps.local.plain_models import ProfilePainModel, ProfilePassportPlainModel, \
    OfficialAddressPlainModel, RealAddressPlainModel, PersonalInformationPlainModel, PlacementPlainModel, \
    AdditionalIncomePlainModel, ChargesPlainModel, AssetsPlainModel
from django.utils.translation import ugettext_lazy as _


class LocalScoringFacade(BaseScoringFacade, BaseFacade):
    local_scoring_actions = LocalScoringActions()

    def process_request(self, data):
        self.check_mandatory_parameters(data)
        user_data = self.generate_user_data(data)
        scoring = self.local_scoring_actions.generate_score(user_data)
        return scoring

    def generate_user_data(self, data):
        profile_passport_data = ProfilePassportPlainModel(**data)
        official_address_data = OfficialAddressPlainModel(**data)
        real_address_data = RealAddressPlainModel(**data)
        personal_profile_data = PersonalInformationPlainModel(**data)
        placement_profile_data = PlacementPlainModel(**data)
        additional_income_data = AdditionalIncomePlainModel(**data)
        charges_profile_data = ChargesPlainModel(**data)
        assets_profile_data = AssetsPlainModel(**data)
        profile_data = ProfilePainModel(
            profile_passport_information=profile_passport_data,
            profile_official_address=official_address_data,
            profile_real_address=real_address_data,
            profile_personal_information=personal_profile_data,
            profile_placement_information=placement_profile_data,
            profile_additional_income=additional_income_data,
            profile_charges=charges_profile_data,
            profile_assets=assets_profile_data,
            **data)
        return profile_data