# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.scoring_cards.AssetScoringCard import AssetScoringCard
from django.utils.translation import ugettext_lazy as _


class AssetScoringModule(BaseScoringModule):
    cards = AssetScoringCard()

    # 'assets_deposits_amount',
    # 'assets_deposits_monthly_percents',
    # 'assets_deposits_maturity_date',
    # 'assets_other_assets_price',

    def calculate_score(self, data):
        available_assets_score = self.calculate_available_assets_score(data)
        print 'available assets score: %s' % available_assets_score
        car_score = self.calculate_car_score(data)
        print 'car score: %s' % car_score
        total_assets_score = available_assets_score + car_score
        return total_assets_score

    def calculate_available_assets_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_assets, 'assets_available_assets'):
            score = self.cards.get_available_assets_card()[getattr(data.profile_assets, 'assets_available_assets')[0]]
        return score

    def calculate_flat_score(self, data):
        area_score = self.calculate_flat_area_score(data)
        'flat area score: %s' % area_score
        status_score = self.calculate_flat_status_score(data)
        'flat status score: %s' % status_score
        total_score = area_score + status_score
        return total_score

    def calculate_flat_area_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_flat_area'):
            flat_area = getattr(data.profile_assets, 'assets_flat_area')[0]
            if flat_area >= self.cards.max_flat_area:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_flat_area_card(),
                                   key=lambda key: self.cards.get_flat_area_card()[key], reverse=True):
                    if flat_area < float(item):
                        score = self.cards.get_flat_area_card()[item]
                        break
        return score

    def calculate_flat_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_flat_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_flat_state')[0]]
        return score

    def calculate_house_score(self, data):
        area_score = self.calculate_house_area_score(data)
        'house area score: %s' % area_score
        status_score = self.calculate_house_status_score(data)
        'house status score: %s' % status_score
        total_score = area_score + status_score
        return total_score

    def calculate_house_area_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_house_area'):
            house_area = getattr(data.profile_assets, 'assets_house_area')[0]
            if house_area >= self.cards.max_house_area:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_house_area_card(),
                                   key=lambda key: self.cards.get_house_area_card()[key], reverse=True):
                    if house_area < float(item):
                        score = self.cards.get_house_area_card()[item]
                        break
        return score

    def calculate_house_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_house_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_house_state')[0]]
        return score

    def calculate_car_score(self, data):
        status_score = self.calculate_car_status_score(data)
        print 'car status score: %s' % status_score
        lifetime_score = self.calculate_car_year_manufacture_score(data)
        print 'car lifetime score: %s' % lifetime_score
        mileage_car = self.calculate_car_mileage_score(data)
        print 'car mileage score: %s' % mileage_car
        total_score = status_score + lifetime_score + mileage_car
        return total_score

    def calculate_car_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_car_state')[0]]
        return score

    def calculate_car_year_manufacture_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_year_manufacture'):
            car_year = int(getattr(data.profile_assets, 'assets_car_year_manufacture')[0])
            current_year = datetime.datetime.today().year
            year = abs(current_year - car_year)
            if not int(year) >= self.cards.max_car_lifetime_years:
                for item in sorted(self.cards.get_car_lifetime_card(),
                                   key=lambda key: self.cards.get_car_lifetime_card()[key], reverse=True):
                    if int(year) < int(item):
                        score = self.cards.get_car_lifetime_card()[item]
                        break
        return score

    def calculate_car_mileage_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_mileage'):
            mileage = int(getattr(data.profile_assets, 'assets_car_mileage')[0])
            if not int(mileage) >= self.cards.max_car_mileage:
                for item in sorted(self.cards.get_car_mileage_card(),
                                   key=lambda key: self.cards.get_car_mileage_card()[key], reverse=True):
                    if int(mileage) < int(item):
                        score = self.cards.get_car_mileage_card()[item]
                        break
        return score