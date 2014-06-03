# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext_lazy as _


class ProfilePainModel(BasePlainModel):
    fields = [
        'profile_third_name',
        'profile_birthday',
        'profile_gender',
        'profile_location',
        'profile_citizenship',
        'profile_passport_information',
        'profile_official_address',
        'profile_real_address',
        'profile_personal_information',
        'profile_placement_information',
        'profile_additional_income',
        'profile_charges',
        'profile_assets',
    ]


class ProfilePassportPlainModel(BasePlainModel):
    fields = [
        'passport_series',
        'passport_number',
        'passport_date',
        'passport_issue_by',
        'passport_pdn'
    ]


class OfficialAddressPlainModel(BasePlainModel):
    fields = [
        'official_country',
        'official_region',
        'official_city',
        'official_street',
        'official_house',
        'official_additional_information',
        'official_flat_number',
        'official_postcode',
    ]


class RealAddressPlainModel(BasePlainModel):
    fields = [
        'real_country',
        'real_region',
        'real_city',
        'real_street',
        'real_house',
        'real_additional_information',
        'real_flat_number',
        'real_postcode',
    ]


class PersonalInformationPlainModel(BasePlainModel):
    fields = [
        'personal_education',
        'personal_marital_status',
        'personal_cohabitants',
        'personal_dependents',
    ]


class PlacementPlainModel(BasePlainModel):
    fields = [
        'placement_type',
        'placement_organisation_count_employees',
        'placement_position',
        'placement_category_position',
        'placement_income',
        'placement_pdn_organisation',
        'placement_term',
        'placement_tax_quarter',
        'placement_additional_income',
        'placement_charges',
    ]


class AdditionalIncomePlainModel(BasePlainModel):
    fields = [
        'additional_income_presence',
        'additional_income_type_income',
        'additional_income_amount',
    ]


class ChargesPlainModel(BasePlainModel):
    fields = [
        'charges_food',
        'charges_health',
        'charges_clothes',
        'charges_utilities',
        'charges_rent',
        'charges_alimony',
        'charges_outstanding_loans ',
        'charges_finance_organisation',
        'charges_purpose_credit',
        'charges_currency_credit',
        'charges_maturity_date',
        'charges_initial_amount',
        'charges_current_amount',
        'charges_monthly_payment',
    ]


class AssetsPlainModel(BasePlainModel):
    fields = [
        'assets_available_assets',
        'assets_flat',
        'assets_flat_address',
        'assets_flat_area',
        'assets_flat_state',
        'assets_house',
        'assets_house_address',
        'assets_house_area',
        'assets_house_state',
        'assets_car',
        'assets_car_mark',
        'assets_car_model',
        'assets_car_year_manufacture',
        'assets_car_mileage',
        'assets_car_state',
        'assets_deposits',
        'assets_deposits_amount',
        'assets_deposits_monthly_percents',
        'assets_deposits_maturity_date',
        'assets_other_assets',
        'assets_other_assets_title',
        'assets_other_assets_price',
    ]