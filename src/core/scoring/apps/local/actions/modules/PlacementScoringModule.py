# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementCleanIncomeCardActions import \
    LocalPlacementCleanIncomeCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementIncomeCardActions import \
    LocalPlacementIncomeCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementPeEmployeesCardActions import \
    LocalPlacementPeEmployeesCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementPeTaxCardActions import \
    LocalPlacementPeTaxCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementPeTermCardActions import \
    LocalPlacementPeTermCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementTypeCardActions import \
    LocalPlacementTypeCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementWageCategoryCardActions import \
    LocalPlacementWageCategoryCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementWageEarnAmountCardActions import \
    LocalPlacementWageEarnAmountCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.actions.LocalPlacementWageTermCardActions import \
    LocalPlacementWageTermCardActions
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementWageCategoryCard
from core.scoring.apps.local.scoring_cards.placement_cards.plain_models import LocalPlacementWageCategoryCardPlainModel, \
    LocalPlacementTypeCardPlainModel
from core.scoring.apps.local.services.LocalPlacementScoringService import LocalPlacementScoringService
from core.scoring.apps.local.services.LocalStaticDataService import LocalStaticDataService
from django.utils.translation import ugettext as _
from core.scoring.apps.local.plain_models import ChargesPlainModel, LocalPlacementScoringPlainModel, \
    LocalStaticDataPlainModel
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule


class PlacementScoringModule(BaseScoringModule):
    placement_service = LocalPlacementScoringService()
    type_actions = LocalPlacementTypeCardActions()
    pe_term_actions = LocalPlacementPeTermCardActions()
    pe_employees_actions = LocalPlacementPeEmployeesCardActions()
    pe_tax_actions = LocalPlacementPeTaxCardActions()
    wage_term_actions = LocalPlacementWageTermCardActions()
    wage_category_actions = LocalPlacementWageCategoryCardActions()
    wage_amount_actions = LocalPlacementWageEarnAmountCardActions()
    income_actions = LocalPlacementIncomeCardActions()
    clean_income_actions = LocalPlacementCleanIncomeCardActions()
    static_data_service = LocalStaticDataService()

    def calculate_score(self, data):
        placement_type_score = self.calculate_type_score(data)
        print 'placement type score: %s' % placement_type_score.placement_type_score
        placement_income_score = self.calculate_income_score(data)
        print 'placement income score: %s' % placement_income_score.placement_income_score
        placement_clean_income = self.calculate_clean_income(data)
        print 'placement clean income score: %s' % placement_clean_income.placement_clean_income
        work_score = self.calculate_work_scores(data)
        print 'work score: %s' % work_score.work_score
        total_score = placement_type_score.placement_type_score + \
                      placement_income_score.placement_income_score + \
                      placement_clean_income.placement_clean_income + \
                      work_score.work_score
        placement_data = dict(placement_type_score.__dict__.items() + placement_income_score.__dict__.items() +
                              placement_clean_income.__dict__.items() + work_score.__dict__.items())
        data = LocalPlacementScoringPlainModel(total_score=total_score, **placement_data)
        placement_data = self.placement_service.create(data)
        return placement_data

    def calculate_work_scores(self, data):
        work_data = LocalPlacementScoringPlainModel()
        if hasattr(data.profile_placement_information, 'placement_type'):
            if int(getattr(data.profile_placement_information, 'placement_type')) == \
                    self.type_actions.service.model_instance.TYPE_PRIVATE_ENTREPRENEUR:
                work_data = self.calculate_score_for_pe(data)
            if int(getattr(data.profile_placement_information, 'placement_type')) == \
                    self.type_actions.service.model_instance.TYPE_WAGE_EARNER:
                work_data = self.calculate_score_for_employment_user(data)
        score = 0
        for field in LocalPlacementScoringPlainModel().fields:
            if hasattr(work_data, field):
                score += int(getattr(work_data, field))
        score = self.type_actions.get_min_score() if not score else score
        data = LocalPlacementScoringPlainModel(work_score=score, **work_data.__dict__)
        return data

    def calculate_score_for_pe(self, data):
        term_score = self.calculate_pe_term_score(data)
        print 'pe term score: %s' % term_score
        tax_score = self.calculate_pe_tax_score(data)
        print 'pe tax score: %s' % tax_score
        count_score = self.calculate_pe_count_employees_score(data)
        print 'pe count employees score: %s' % count_score
        data = LocalPlacementScoringPlainModel(tax_score=tax_score, count_employees_score=count_score,
                                               term_score=term_score)
        return data

    def calculate_pe_term_score(self, data):
        score = self.pe_term_actions.get_min_score()
        term = int(getattr(data.profile_placement_information, 'placement_term')) * 12 if \
            hasattr(data.profile_placement_information, 'placement_term') else 0
        if term >= self.pe_term_actions.get_max_key():
                score = self.pe_term_actions.get_max_score()
        else:
            for item in self.pe_term_actions.get_card():
                if term <= item.key:
                    score = item.value
                    break
        return score

    def calculate_pe_count_employees_score(self, data):
        score = self.pe_employees_actions.get_min_score()
        if hasattr(data.profile_placement_information, 'placement_organisation_count_employees'):
            count = int(getattr(data.profile_placement_information, 'placement_organisation_count_employees'))
            if count >= self.pe_employees_actions.get_max_key():
                score = self.pe_employees_actions.get_max_score()
            else:
                for item in self.pe_employees_actions.get_card():
                    if count <= item.key:
                        score = item.value
                        break
        return score

    def calculate_pe_tax_score(self, data):
        score = self.pe_tax_actions.get_min_score()
        if hasattr(data.profile_placement_information, 'placement_tax_quarter'):
            tax = int(getattr(data.profile_placement_information, 'placement_tax_quarter'))
            if tax >= self.pe_tax_actions.get_max_key():
                score = self.pe_tax_actions.get_max_score()
            else:
                for item in self.pe_tax_actions.get_card():
                    if tax <= item.key:
                        score = item.value
                        break
        return score

    def calculate_score_for_employment_user(self, data):
        term_score = self.calculate_employment_term_score(data)
        print 'employment term score: %s' % term_score
        wage_amount_score = self.calculate_employment_wage_amount_score(data)
        print 'employment wage amount score: %s' % wage_amount_score
        category_position_score = self.calculate_category_position(data)
        print 'category position score: %s' % category_position_score
        data = LocalPlacementScoringPlainModel(term_score=term_score, wage_score=wage_amount_score,
                                               category_position_score=category_position_score,)
        return data

    def calculate_employment_term_score(self, data):
        score = self.wage_term_actions.get_min_score()
        term = int(getattr(data.profile_placement_information, 'placement_term')) * 12 if \
            hasattr(data.profile_placement_information, 'placement_term') else 0
        if term >= self.wage_term_actions.get_max_key():
            score = self.wage_term_actions.get_max_score()
        else:
            for item in self.wage_term_actions.get_card():
                if term <= item.key:
                    score = item.value
                    break
        return score

    def calculate_category_position(self, data):
        score = self.wage_category_actions.get_min_score()
        if hasattr(data.profile_placement_information, 'placement_category_position'):
            category_position = int(getattr(data.profile_placement_information, 'placement_category_position'))
            data = LocalPlacementWageCategoryCardPlainModel(key=category_position)
            score = self.wage_category_actions.service.get_item(**data.__dict__).value if \
                self.wage_category_actions.service.get_item(**data.__dict__) else \
                self.wage_category_actions.get_min_score()
        return score

    def calculate_employment_wage_amount_score(self, data):
        score = self.wage_amount_actions.get_min_score()
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income)
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            income += float(getattr(data.profile_placement_information, 'placement_additional_income'))
        if income >= float(self.wage_amount_actions.get_max_key()):
            score = self.wage_amount_actions.get_max_score()
        else:
            for item in self.wage_amount_actions.get_card():
                if income < float(item.key):
                    score = item.value
                    break
        return score

    def calculate_type_score(self, data):
        score = self.type_actions.get_min_score()
        if hasattr(data.profile_placement_information, 'placement_type'):
            data = LocalPlacementTypeCardPlainModel(key=int(data.profile_placement_information.placement_type))
            score = self.type_actions.service.get_item(**data.__dict__).value if \
                self.type_actions.service.get_item(**data.__dict__) else self.type_actions.get_min_score()
        data = LocalPlacementScoringPlainModel(placement_type_score=score)
        return data

    def calculate_income_score(self, data):
        score = self.income_actions.get_min_score()
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income) if \
                getattr(data.profile_placement_information, 'placement_income') else 0
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            income += float(getattr(data.profile_placement_information, 'placement_additional_income')) if \
                getattr(data.profile_placement_information, 'placement_additional_income') else 0
        if income >= float(self.income_actions.get_max_key()):
            score = self.income_actions.get_max_score()
        else:
            for item in self.income_actions.get_card():
                if income < float(item.key):
                    score = item.value
                    break
        data = LocalPlacementScoringPlainModel(placement_income_score=score)
        return data

    def calculate_clean_income(self, data):
        score = self.clean_income_actions.get_min_score()
        charges = income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income) if \
                getattr(data.profile_placement_information, 'placement_income') else 0
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            income += float(getattr(data.profile_placement_information, 'placement_additional_income')) if \
                getattr(data.profile_placement_information, 'placement_additional_income') else 0

        # for item in ChargesPlainModel().fields:
        #     if hasattr(data.profile_charges, item):
        #         charges += float(getattr(data.profile_charges, item)) if \
        #             getattr(data.profile_charges, item) else 0

        if hasattr(data.profile_official_address, 'official_region'):
            static = self.static_data_service.get_item(
                region=getattr(data.profile_official_address, 'official_region'),
                country__title=getattr(data, 'country'))
            for key, value in static.__dict__.iteritems():
                if key in LocalStaticDataPlainModel().fields and isinstance(value, long) and 'wage' not in key:
                    charges += int(value)

        clean_income = income - charges
        if clean_income >= self.clean_income_actions.get_max_key():
            score = self.clean_income_actions.get_max_score()
        else:
            for item in self.clean_income_actions.get_card():
                if income < float(item.key):
                    score = item.value
                    break
        data = LocalPlacementScoringPlainModel(placement_clean_income=score)
        return data