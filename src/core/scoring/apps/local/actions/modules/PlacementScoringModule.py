# -*- coding: utf-8 -*-
from core.scoring.apps.local.services.LocalPlacementScoringService import LocalPlacementScoringService
from django.utils.translation import ugettext as _
from core.scoring.apps.local.plain_models import ChargesPlainModel, LocalPlacementScoringPlainModel
from core.scoring.apps.local.scoring_cards.PlacementInformationCards import PlacementInformationCards
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule


class PlacementScoringModule(BaseScoringModule):
    cards = PlacementInformationCards()
    placement_service = LocalPlacementScoringService()

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
        # score = self.cards.min_score
        work_data = LocalPlacementScoringPlainModel()
        if hasattr(data.profile_placement_information, 'placement_type'):
            if int(getattr(data.profile_placement_information, 'placement_type')[0]) == \
                self.cards.TYPE_PRIVATE_ENTREPRENEUR:
                # score = self.calculate_score_for_pe(data)
                work_data = self.calculate_score_for_pe(data)
            if int(getattr(data.profile_placement_information, 'placement_type')[0]) == \
                self.cards.TYPE_WAGE_EARNER:
                # score = self.calculate_score_for_employment_user(data)
                work_data = self.calculate_score_for_employment_user(data)
        score = 0
        for field in LocalPlacementScoringPlainModel.fields:
            if hasattr(work_data, field):
                try:
                    score += int(getattr(work_data, field))
                except Exception:
                    continue
        score = self.cards.min_score if not score else score
        data = LocalPlacementScoringPlainModel(work_score=score, **work_data.__dict__)
        return data

    def calculate_score_for_pe(self, data):
        term_score = self.calculate_pe_term_score(data)
        print 'pe term score: %s' % term_score
        tax_score = self.calculate_pe_tax_score(data)
        print 'pe tax score: %s' % tax_score
        count_score = self.calculate_pe_count_employees_score(data)
        print 'pe count employees score: %s' % count_score
        # score = term_score + tax_score
        data = LocalPlacementScoringPlainModel(tax_score=tax_score, count_employees_score=count_score,
                                               term_score=term_score)
        return data

    def calculate_pe_term_score(self, data):
        score = self.cards.min_employ_score
        if hasattr(data.profile_placement_information, 'placement_term'):
            try:
                term = int(getattr(data.profile_placement_information, 'placement_term')[0])
                if term >= self.cards.max_employ_term:
                    score = self.cards.max_employ_score
                else:
                    for item in sorted(self.cards.get_pe_term_card(),
                                       key=lambda key: self.cards.get_pe_term_card()[key]):
                        if term <= int(item):
                            score = self.cards.get_pe_term_card()[item]
                            break
            except Exception:
                score = self.cards.min_employ_score
        return score

    def calculate_pe_tax_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_placement_information, 'placement_organisation_count_employees'):
            try:
                count = int(getattr(data.profile_placement_information, 'placement_organisation_count_employees')[0])
                if count >= self.cards.max_pe_employees_count:
                    score = self.cards.max_score
                else:
                    for item in sorted(self.cards.get_pe_count_employments_card(),
                                       key=lambda key: self.cards.get_pe_count_employments_card()[key]):
                        if count <= int(item):
                            score = self.cards.get_pe_count_employments_card()[item]
                            break
            except Exception:
                score = self.cards.min_score
        return score

    def calculate_pe_count_employees_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_placement_information, 'placement_tax_quarter'):
            try:
                tax = int(getattr(data.profile_placement_information, 'placement_tax_quarter')[0])
                if tax >= self.cards.max_pe_tax_amount:
                    score = self.cards.max_score
                else:
                    for item in sorted(self.cards.get_pe_tax_card(),
                                       key=lambda key: self.cards.get_pe_tax_card()[key]):
                        if tax <= int(item):
                            score = self.cards.get_pe_tax_card()[item]
                            break
            except Exception:
                score = self.cards.min_score
        return score

    def calculate_score_for_employment_user(self, data):
        term_score = self.calculate_employment_term_score(data)
        print 'employment term score: %s' % term_score
        wage_score = self.calculate_employment_wage_score(data)
        print 'employment wage score: %s' % wage_score
        category_position_score = self.calculate_category_position(data)
        print 'category position score: %s' % category_position_score
        # score = term_score + wage_score + category_position_score
        data = LocalPlacementScoringPlainModel(term_score=term_score, wage_score=wage_score,
                                               category_position_score=category_position_score,)
        return data

    def calculate_employment_term_score(self, data):
        score = self.cards.min_employ_score
        if hasattr(data.profile_placement_information, 'placement_term'):
            try:
                term = int(getattr(data.profile_placement_information, 'placement_term')[0])
                if term >= self.cards.max_employ_term:
                    score = self.cards.max_employ_score
                else:
                    for item in sorted(self.cards.get_wage_earner_term_card(),
                                       key=lambda key: self.cards.get_wage_earner_term_card()[key]):
                        if term <= int(item):
                            score = self.cards.get_wage_earner_term_card()[item]
                            break
            except Exception:
                score = self.cards.min_employ_score
        return score

    def calculate_category_position(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_placement_information, 'placement_category_position'):
            try:
                category_position = int(getattr(data.profile_placement_information, 'placement_category_position')[0])
                for item in sorted(self.cards.get_wage_earner_term_card(),
                                   key=lambda key: self.cards.get_wage_earner_term_card()[key]):
                    if category_position == int(item):
                        score = self.cards.get_wage_earner_category_postition_card()[item]
                        break
            except Exception:
                score = self.cards.min_score
        return score

    def calculate_employment_wage_score(self, data):
        score = self.cards.min_income_score
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            try:
                income = float(data.profile_placement_information.placement_income[0])
            except Exception:
                income = 0
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            try:
                income += float(getattr(data.profile_placement_information, 'placement_additional_income')[0])
            except Exception:
                income += 0
        if income >= self.cards.max_income_amount:
            score = self.cards.max_income_score
        else:
            try:
                for item in sorted(self.cards.get_wage_earner_amount_card(),
                                   key=lambda key: self.cards.get_wage_earner_amount_card()[key]):
                    if income < float(item):
                        score = self.cards.get_wage_earner_amount_card()[item]
                        break
            except Exception:
                score = self.cards.min_income_score
        return score

    def calculate_type_score(self, data):
        score = self.cards.min_type_score
        if hasattr(data.profile_placement_information, 'placement_type'):
            score = self.cards.get_placement_type_card()[str(data.profile_placement_information.placement_type[0])]
        data = LocalPlacementScoringPlainModel(placement_type_score=score)
        return data

    def calculate_income_score(self, data):
        score = self.cards.min_income_score
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            try:
                income = float(data.profile_placement_information.placement_income[0]) if \
                    getattr(data.profile_placement_information, 'placement_income') else 0
            except Exception:
                income = 0
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            try:
                income += float(getattr(data.profile_placement_information, 'placement_additional_income')[0]) if \
                    getattr(data.profile_placement_information, 'placement_additional_income') else 0
            except Exception:
                income = 0
        if income >= self.cards.max_income_amount:
            score = self.cards.max_income_score
        else:
            for item in sorted(self.cards.get_placement_income_card(),
                               key=lambda key: self.cards.get_placement_income_card()[key]):
                if income < float(item):
                    score = self.cards.get_placement_income_card()[item]
                    break
        data = LocalPlacementScoringPlainModel(placement_income_score=score)
        return data

    def calculate_clean_income(self, data):
        score = self.cards.min_clean_income_score
        charges = income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            try:
                income = float(data.profile_placement_information.placement_income[0]) if \
                    getattr(data.profile_placement_information, 'placement_income') else 0
            except Exception:
                income = 0
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            try:
                income += float(getattr(data.profile_placement_information, 'placement_additional_income')[0]) if \
                    getattr(data.profile_placement_information, 'placement_additional_income') else 0
            except Exception:
                income = 0
        for item in ChargesPlainModel.fields:
            if hasattr(data.profile_charges, item):
                try:
                    charges += float(getattr(data.profile_charges, item)[0]) if \
                        getattr(data.profile_charges, item) else 0
                except Exception:
                    continue
        clean_income = income - charges
        if clean_income >= self.cards.max_clean_income_amount:
            score = self.cards.max_clean_income_score
        else:
            for item in sorted(self.cards.get_placement_clean_income_card(),
                               key=lambda key: self.cards.get_placement_clean_income_card()[key]):
                if income < float(item):
                    score = self.cards.get_placement_clean_income_card()[item]
                    break
        data = LocalPlacementScoringPlainModel(placement_clean_income=score)
        return data