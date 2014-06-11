# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalAssetsScoringPlainModel
from core.scoring.apps.local.scoring_cards.AssetScoringCard import AssetScoringCard
from core.scoring.apps.local.services.LocalAssetsScoringService import LocalAssetsScoringService
from django.utils.translation import ugettext_lazy as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class AssetScoringModule(BaseScoringModule):
    cards = AssetScoringCard()
    assets_service = LocalAssetsScoringService()

    def calculate_score(self, data):
        available_assets_score = self.calculate_available_assets_score(data)
        print 'available assets score: %s' % available_assets_score
        flat_data = self.calculate_flat_score(data)
        print 'flat score: %s' % flat_data.flat_score
        house_data = self.calculate_house_score(data)
        print 'house score: %s' % house_data.house_score
        car_data = self.calculate_car_score(data)
        print 'car score: %s' % car_data.car_score
        deposit_data = self.calculate_deposit_score(data)
        print 'deposit score: %s' % deposit_data.deposit_score
        other_assets_score = self.calculate_other_assets_price_score(data)
        print 'other assets score: %s' % other_assets_score
        total_assets_score = available_assets_score + flat_data.flat_score + house_data.house_score + \
                             car_data.car_score + deposit_data.deposit_score + other_assets_score
        assets_generated_data = dict(flat_data.__dict__.items() + house_data.__dict__.items() +
                                     car_data.__dict__.items() + deposit_data.__dict__.items())
        data = LocalAssetsScoringPlainModel(
            available_assets_score=available_assets_score,
            other_assets_score=other_assets_score,
            total_score=total_assets_score,
            **assets_generated_data
        )
        assets_data = self.assets_service.create(data)
        return assets_data

    def calculate_available_assets_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_assets, 'assets_available_assets'):
            score = self.cards.get_available_assets_card()[getattr(data.profile_assets, 'assets_available_assets')[0]]
        return score

    def calculate_other_assets_price_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_other_assets_price'):
            price = int(float(getattr(data.profile_assets, 'assets_other_assets_price')[0]))
            if price >= self.cards.max_other_assets_price:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_other_assets_price_card(),
                                   key=lambda key: self.cards.get_other_assets_price_card()[key]):
                    if price < float(item):
                        score = self.cards.get_other_assets_price_card()[item]
                        break
        return score

    def calculate_flat_score(self, data):
        area_score = self._calculate_flat_area_score(data)
        'flat area score: %s' % area_score
        status_score = self._calculate_flat_status_score(data)
        'flat status score: %s' % status_score
        total_score = area_score + status_score
        data = LocalAssetsScoringPlainModel(flat_score=total_score, flat_area_score=area_score,
                                            flat_status_score=status_score, )
        return data

    def _calculate_flat_area_score(self, data):
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

    def _calculate_flat_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_flat_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_flat_state')[0]]
        return score

    def calculate_house_score(self, data):
        area_score = self._calculate_house_area_score(data)
        'house area score: %s' % area_score
        status_score = self._calculate_house_status_score(data)
        'house status score: %s' % status_score
        total_score = area_score + status_score
        data = LocalAssetsScoringPlainModel(
            house_score=total_score,
            house_area_score=area_score,
            house_status_score=status_score,
        )
        return data

    def _calculate_house_area_score(self, data):
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

    def _calculate_house_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_house_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_house_state')[0]]
        return score

    def calculate_car_score(self, data):
        status_score = self._calculate_car_status_score(data)
        print 'car status score: %s' % status_score
        lifetime_score = self._calculate_car_year_manufacture_score(data)
        print 'car lifetime score: %s' % lifetime_score
        mileage_car_score = self._calculate_car_mileage_score(data)
        print 'car mileage score: %s' % mileage_car_score
        total_score = status_score + lifetime_score + mileage_car_score
        data = LocalAssetsScoringPlainModel(
            car_score=total_score,
            car_status_score=status_score,
            car_lifetime_score=lifetime_score,
            car_mileage_car_score=mileage_car_score,
        )
        return data

    def _calculate_car_status_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_state'):
            score = self.cards.get_assets_status_card()[getattr(data.profile_assets, 'assets_car_state')[0]]
        return score

    def _calculate_car_year_manufacture_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_year_manufacture'):
            car_year = int(getattr(data.profile_assets, 'assets_car_year_manufacture')[0])
            current_year = datetime.datetime.today().year
            year = abs(current_year - car_year)
            if year >= self.cards.max_car_lifetime_years:
                score = self.cards.min_assets_score
            else:
                for item in sorted(self.cards.get_car_lifetime_card(),
                                   key=lambda key: self.cards.get_car_lifetime_card()[key], reverse=True):
                    if int(year) < int(item):
                        score = self.cards.get_car_lifetime_card()[item]
                        break
        return score

    def _calculate_car_mileage_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_car_mileage'):
            mileage = int(getattr(data.profile_assets, 'assets_car_mileage')[0])
            if int(mileage) >= self.cards.max_car_mileage:
                score = self.cards.min_assets_score
            else:
                for item in sorted(self.cards.get_car_mileage_card(),
                                   key=lambda key: self.cards.get_car_mileage_card()[key], reverse=True):
                    if int(mileage) < int(item):
                        score = self.cards.get_car_mileage_card()[item]
                        break
        return score

    def calculate_deposit_score(self, data):
        deposit_amount_score = self._calculate_deposits_amount_score(data)
        print 'deposit amount score: %s' % deposit_amount_score
        deposit_percents_score = self._calculate_deposits_monthly_percents_score(data)
        print 'deposit percents score: %s' % deposit_percents_score
        deposit_maturity_date_score = self._calculate_deposits_maturity_date_score(data)
        print 'deposit maturity date score: %s' % deposit_maturity_date_score
        total_score = deposit_amount_score + deposit_percents_score + deposit_maturity_date_score
        data = LocalAssetsScoringPlainModel(
            deposit_score=total_score,
            deposit_amount_score=deposit_amount_score,
            deposit_percents_score=deposit_percents_score,
            deposit_maturity_date_score=deposit_maturity_date_score,
        )
        return data

    def _calculate_deposits_amount_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_deposits_amount'):
            amount = int(float(getattr(data.profile_assets, 'assets_deposits_amount')[0]))
            if amount >= self.cards.max_deposit_amount:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_deposit_amount_card(),
                                   key=lambda key: self.cards.get_deposit_amount_card()[key]):
                    if int(amount) < int(item):
                        score = self.cards.get_deposit_amount_card()[item]
                        break
        return score

    def _calculate_deposits_monthly_percents_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_deposits_monthly_percents'):
            percents = int(float(getattr(data.profile_assets, 'assets_deposits_monthly_percents')[0]))
            if percents >= self.cards.max_deposit_monthly_percents:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_deposit_monthly_percents_card(),
                                   key=lambda key: self.cards.get_deposit_monthly_percents_card()[key]):
                    if int(percents) < int(item):
                        score = self.cards.get_deposit_monthly_percents_card()[item]
                        break
        return score

    def _calculate_deposits_maturity_date_score(self, data):
        score = self.cards.min_assets_score
        if hasattr(data.profile_assets, 'assets_deposits_maturity_date'):
            maturity_date = datetime.datetime.strptime(
                getattr(data.profile_assets, 'assets_deposits_maturity_date')[0], BASE_DATE_FORMAT)
            current_date = datetime.datetime.now()
            days = abs(maturity_date - current_date).days
            months = int(days / 30)
            if months >= self.cards.max_deposit_maturity_months:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_deposit_maturity_date_card(),
                                   key=lambda key: self.cards.get_deposit_maturity_date_card()[key]):
                    if int(months) < int(item):
                        score = self.cards.get_deposit_maturity_date_card()[item]
                        break
        return score