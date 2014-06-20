# -*- coding: utf-8 -*-
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.apps.local.management.commands.plain_models.AgeScoringCard import AgeScoringCard
from core.scoring.apps.local.management.commands.plain_models.AssetScoringCard import AssetScoringCard
from core.scoring.apps.local.management.commands.plain_models.CountryMillionCityCards import CountryMillionCityCards
from core.scoring.apps.local.management.commands.plain_models.CreditScoringCard import CreditScoringCard
from core.scoring.apps.local.management.commands.plain_models.PersonalInformationCards import PersonalInformationCards
from core.scoring.apps.local.management.commands.plain_models.PlacementInformationCards import PlacementInformationCards
from core.scoring.apps.local.scoring_cards.age_cards.plain_models import LocalAgeScoringCardPlainModel
from core.scoring.apps.local.scoring_cards.age_cards.services.AgeScoringCardService import AgeScoringCardService
from core.scoring.apps.local.scoring_cards.assets_cards.plain_models import LocalAvailableAssetsCardPlainModel, \
    LocalFlatAreaCardPlainModel, LocalFlatStatusCardPlainModel, LocalHouseAreaCardPlainModel, \
    LocalHouseStatusCardPlainModel, LocalCarLifetimeCardPlainModel, LocalCarMileageCardPlainModel, \
    LocalCarStatusCardPlainModel, LocalDepositMaturityDateCardPlainModel, LocalDepositAmountCardPlainModel, \
    LocalDepositMonthlyPercentsCardPlainModel, LocalOtherAssetsPriceCardPlainModel
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalAssetsScoringCardService import \
    LocalAssetsScoringCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarLifetimeService import LocalCarLifetimeService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarMileageCardService import \
    LocalCarMileageCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarStatusCardService import \
    LocalCarStatusCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositAmountCardService import \
    LocalDepositAmountCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMaturityDateCardService import \
    LocalDepositMaturityDateCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMonthlyPercentsCardService import \
    LocalDepositMonthlyPercentsCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatAreaCardService import \
    LocalFlatAreaCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatStatusCardService import \
    LocalFlatStatusCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseAreaCardService import \
    LocalHouseAreaCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseStatusCardService import \
    LocalHouseStatusCardService
from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalOtherAssetsPriceCardService import \
    LocalOtherAssetsPriceCardService
from core.scoring.apps.local.scoring_cards.cities_cards.plain_models import ScoringCityMillionairePlainModel
from core.scoring.apps.local.scoring_cards.cities_cards.services.ScoringCityMillionaireService import \
    ScoringCityMillionaireService
from core.scoring.apps.local.scoring_cards.loan_cards.plain_models import LocalOutstandingLoansCardPlainModel, \
    LocalAmountLoansCardPlainModel, LocalPercentRepaymentLoansCardPlainModel, LocalDaysRepaymentLoansCardPlainModel, \
    LocalMonthlyPaymentLoansCardPlainModel, LocalDebtBurdenLoansCardPlainModel, LocalDependentsCardPlainModel
from core.scoring.apps.local.scoring_cards.loan_cards.services.LoanOutstandingLoansCardService import \
    LoanOutstandingLoansCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalAmountLoansCardService import \
    LocalAmountLoansCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDaysRepaymentLoansCardService import \
    LocalDaysRepaymentLoansCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDebtBurdenLoansCardService import \
    LocalDebtBurdenLoansCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDependentsCardService import \
    LocalDependentsCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalMonthlyPaymentLoansCardService import \
    LocalMonthlyPaymentLoansCardService
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalPercentRepaymentLoansCardService import \
    LocalPercentRepaymentLoansCardService
from core.scoring.apps.local.scoring_cards.personal_cards.plain_models import LocalPersonalEducationCardPlainModel, \
    LocalMaritalStatusBadCardPlainModel, LocalMaritalStatusNormalCardPlainModel, LocalIdentityAddressesCardPlainModel
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalIdentityAddressesCardService import \
    LocalIdentityAddressesCardService
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalMaritalStatusBadCardService import \
    LocalMaritalStatusBadCardService
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalMaritalStatusNormalCardService import \
    LocalMaritalStatusNormalCardService
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalPersonalEducationCardService import \
    LocalPersonalEducationCardService
from core.scoring.apps.local.scoring_cards.placement_cards.plain_models import LocalPlacementTypeCardPlainModel, \
    LocalPlacementIncomeCardPlainModel, LocalPlacementCleanIncomeCardPlainModel, LocalPlacementWageTermCardPlainModel, \
    LocalPlacementWageEarnAmountCardPlainModel, LocalPlacementWageCategoryCardPlainModel, \
    LocalPlacementPeTermCardPlainModel, LocalPlacementPeTaxCardPlainModel, LocalPlacementPeEmployeesCardPlainModel
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementCleanIncomeCardService import \
    LocalPlacementCleanIncomeCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementIncomeCardService import \
    LocalPlacementIncomeCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeEmployeesCardService import \
    LocalPlacementPeEmployeesCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeTaxCardService import \
    LocalPlacementPeTaxCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeTermCardService import \
    LocalPlacementPeTermCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementTypeCardService import \
    LocalPlacementTypeCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageCategoryCardService import \
    LocalPlacementWageCategoryCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageEarnAmountCardService import \
    LocalPlacementWageEarnAmountCardService
from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageTermCardService import \
    LocalPlacementWageTermCardService
from django.utils.translation import ugettext_lazy as _
from django.core.management import BaseCommand


class Command(BaseCommand):
    age_card = AgeScoringCard()
    age_card_service = AgeScoringCardService()
    assets_card = AssetScoringCard()
    assets_available_service = LocalAssetsScoringCardService()
    assets_flat_area_service = LocalFlatAreaCardService()
    assets_flat_status_service = LocalFlatStatusCardService()
    assets_house_area_service = LocalHouseAreaCardService()
    assets_house_status_service = LocalHouseStatusCardService()
    assets_car_lifetime_service = LocalCarLifetimeService()
    assets_car_mileage_service = LocalCarMileageCardService()
    assets_car_status_service = LocalCarStatusCardService()
    assets_deposit_maturity_service = LocalDepositMaturityDateCardService()
    assets_deposit_amount_service = LocalDepositAmountCardService()
    assets_deposit_percents_service = LocalDepositMonthlyPercentsCardService()
    assets_other_price_service = LocalOtherAssetsPriceCardService()
    cities_card = CountryMillionCityCards()
    country_service = CountryService()
    city_service = ScoringCityMillionaireService()
    loan_card = CreditScoringCard()
    loan_outstanding_service = LoanOutstandingLoansCardService()
    loan_amount_service = LocalAmountLoansCardService()
    loan_amount_percents_service = LocalPercentRepaymentLoansCardService()
    loan_days_to_repayment_service = LocalDaysRepaymentLoansCardService()
    loan_monthly_payment_service = LocalMonthlyPaymentLoansCardService()
    loan_debt_burden_service = LocalDebtBurdenLoansCardService()
    dependents_service = LocalDependentsCardService()
    personal_cards = PersonalInformationCards()
    personal_education_service = LocalPersonalEducationCardService()
    personal_marital_bad_service = LocalMaritalStatusBadCardService()
    personal_marital_normal_service = LocalMaritalStatusNormalCardService()
    personal_identity_addresses_service = LocalIdentityAddressesCardService()
    placement_cards = PlacementInformationCards()
    placement_type_service = LocalPlacementTypeCardService()
    placement_income_service = LocalPlacementIncomeCardService()
    placement_clean_income_service = LocalPlacementCleanIncomeCardService()
    placement_wage_term_service = LocalPlacementWageTermCardService()
    placement_wage_amount_service = LocalPlacementWageEarnAmountCardService()
    placement_wage_category_service = LocalPlacementWageCategoryCardService()
    placement_pe_term_service = LocalPlacementPeTermCardService()
    placement_pe_tax_service = LocalPlacementPeTaxCardService()
    placement_pe_employees_service = LocalPlacementPeEmployeesCardService()

    def handle(self, *args, **options):
        self.fill_age_cards()
        self.fill_assets_cards()
        self.fill_cities_cards()
        self.fill_loan_cards()
        self.fill_personal_cards()
        self.fill_placement_cards()

    def fill_age_cards(self):
        for key, value in self.age_card.get_age_scoring_card().iteritems():
            data = LocalAgeScoringCardPlainModel(key=int(key), value=value)
            self.age_card_service.create(data)

    def fill_assets_cards(self):
        ## available assets
        for key, value in self.assets_card.get_available_assets_card().iteritems():
            data = LocalAvailableAssetsCardPlainModel(key=int(key), value=value)
            self.assets_available_service.create(data)
        ## flat area
        for key, value in self.assets_card.get_flat_area_card().iteritems():
            data = LocalFlatAreaCardPlainModel(key=int(key), value=value)
            self.assets_flat_area_service.create(data)
        ## flat status
        for key, value in self.assets_card.get_assets_status_card().iteritems():
            data = LocalFlatStatusCardPlainModel(key=int(key), value=value)
            self.assets_flat_status_service.create(data)
        ## house area
        for key, value in self.assets_card.get_house_area_card().iteritems():
            data = LocalHouseAreaCardPlainModel(key=int(key), value=value)
            self.assets_house_area_service.create(data)
        ## house status
        for key, value in self.assets_card.get_assets_status_card().iteritems():
            data = LocalHouseStatusCardPlainModel(key=int(key), value=value)
            self.assets_house_status_service.create(data)
        ## car lifetime
        for key, value in self.assets_card.get_car_lifetime_card().iteritems():
            data = LocalCarLifetimeCardPlainModel(key=int(key), value=value)
            self.assets_car_lifetime_service.create(data)
        ## car mileage
        for key, value in self.assets_card.get_car_mileage_card().iteritems():
            data = LocalCarMileageCardPlainModel(key=int(key), value=value)
            self.assets_car_mileage_service.create(data)
        ## car status
        for key, value in self.assets_card.get_assets_status_card().iteritems():
            data = LocalCarStatusCardPlainModel(key=int(key), value=value)
            self.assets_car_status_service.create(data)
        ## deposit maturity
        for key, value in self.assets_card.get_deposit_maturity_date_card().iteritems():
            data = LocalDepositMaturityDateCardPlainModel(key=int(key), value=value)
            self.assets_deposit_maturity_service.create(data)
        ## deposit amount
        for key, value in self.assets_card.get_deposit_amount_card().iteritems():
            data = LocalDepositAmountCardPlainModel(key=int(key), value=value)
            self.assets_deposit_amount_service.create(data)
        ## deposit percents
        for key, value in self.assets_card.get_deposit_monthly_percents_card().iteritems():
            data = LocalDepositMonthlyPercentsCardPlainModel(key=int(key), value=value)
            self.assets_deposit_percents_service.create(data)
        ## other assets
        for key, value in self.assets_card.get_other_assets_price_card().iteritems():
            data = LocalOtherAssetsPriceCardPlainModel(key=int(key), value=value)
            self.assets_other_price_service.create(data)

    def fill_cities_cards(self):
        country = self.country_service.get_current()
        for title in self.cities_card._get_ua_cities():
            data = ScoringCityMillionairePlainModel(country=country, title=title)
            self.city_service.create(data)

    def fill_loan_cards(self):
        ## outstanding loan
        for key, value in self.loan_card.get_current_credit_card().iteritems():
            data = LocalOutstandingLoansCardPlainModel(key=int(key), value=value)
            self.loan_outstanding_service.create(data)
        ## loan amount
        for key, value in self.loan_card.get_credit_amount_card().iteritems():
            data = LocalAmountLoansCardPlainModel(key=int(key), value=value)
            self.loan_amount_service.create(data)
        ## loan percents of repayment
        for key, value in self.loan_card.get_percent_repayment_card().iteritems():
            data = LocalPercentRepaymentLoansCardPlainModel(key=int(key), value=value)
            self.loan_amount_percents_service.create(data)
        ## loan days to repayment
        for key, value in self.loan_card.get_days_to_repayment_card().iteritems():
            data = LocalDaysRepaymentLoansCardPlainModel(key=int(key), value=value)
            self.loan_days_to_repayment_service.create(data)
        ## loan monthly payment
        for key, value in self.loan_card.get_amount_monthly_payment_card().iteritems():
            data = LocalMonthlyPaymentLoansCardPlainModel(key=int(key), value=value)
            self.loan_monthly_payment_service.create(data)
        ## loan debt burden
        for key, value in self.loan_card.get_debt_burden_card().iteritems():
            data = LocalDebtBurdenLoansCardPlainModel(key=float(key), value=value)
            self.loan_debt_burden_service.create(data)
        ## dependents
        for key, value in self.loan_card.get_count_dependents_card().iteritems():
            data = LocalDependentsCardPlainModel(key=int(key), value=value)
            self.dependents_service.create(data)

    def fill_personal_cards(self):
        ## education
        for key, value in self.personal_cards.get_education_card().iteritems():
            data = LocalPersonalEducationCardPlainModel(key=int(key), value=value)
            self.personal_education_service.create(data)
        ## marital status bad
        for key, value in self.personal_cards.get_marital_status_bad_card().iteritems():
            data = LocalMaritalStatusBadCardPlainModel(key=int(key), value=value)
            self.personal_marital_bad_service.create(data)
        ## marital status normal
        for key, value in self.personal_cards.get_marital_status_normal_card().iteritems():
            data = LocalMaritalStatusNormalCardPlainModel(key=int(key), value=value)
            self.personal_marital_normal_service.create(data)
        ## identity addresses
        for key, value in self.personal_cards.get_identity_addresses_card().iteritems():
            data = LocalIdentityAddressesCardPlainModel(key=int(key), value=value)
            self.personal_identity_addresses_service.create(data)

    def fill_placement_cards(self):
        ## placement type
        for key, value in self.placement_cards.get_placement_type_card().iteritems():
            data = LocalPlacementTypeCardPlainModel(key=int(key), value=value)
            self.placement_type_service.create(data)
        ## placement income
        for key, value in self.placement_cards.get_placement_income_card().iteritems():
            data = LocalPlacementIncomeCardPlainModel(key=int(float(key)), value=value)
            self.placement_income_service.create(data)
        ## placement clean income
        for key, value in self.placement_cards.get_placement_clean_income_card().iteritems():
            data = LocalPlacementCleanIncomeCardPlainModel(key=int(key), value=value)
            self.placement_clean_income_service.create(data)
        ## placement wage term
        for key, value in self.placement_cards.get_wage_earner_term_card().iteritems():
            data = LocalPlacementWageTermCardPlainModel(key=int(key), value=value)
            self.placement_wage_term_service.create(data)
        ## placement wage amount
        for key, value in self.placement_cards.get_wage_earner_amount_card().iteritems():
            data = LocalPlacementWageEarnAmountCardPlainModel(key=int(key), value=value)
            self.placement_wage_amount_service.create(data)
        ## placement wage category
        for key, value in self.placement_cards.get_wage_earner_category_postition_card().iteritems():
            data = LocalPlacementWageCategoryCardPlainModel(key=int(key), value=value)
            self.placement_wage_category_service.create(data)
        ## placement pe term
        for key, value in self.placement_cards.get_pe_term_card().iteritems():
            data = LocalPlacementPeTermCardPlainModel(key=int(key), value=value)
            self.placement_pe_term_service.create(data)
        ## placement pe tax
        for key, value in self.placement_cards.get_pe_tax_card().iteritems():
            data = LocalPlacementPeTaxCardPlainModel(key=int(key), value=value)
            self.placement_pe_tax_service.create(data)
        ## placement pe employees
        for key, value in self.placement_cards.get_pe_count_employments_card().iteritems():
            data = LocalPlacementPeEmployeesCardPlainModel(key=int(key), value=value)
            self.placement_pe_employees_service.create(data)