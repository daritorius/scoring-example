# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalAssetsScoringPlainModel, AssetsPlainModel
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalAvailableAssetsScoringCardActions import \
    LocalAvailableAssetsScoringCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalCarLifetimeCardActions import \
    LocalCarLifetimeCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalCarMileageCardActions import \
    LocalCarMileageCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalCarStatusCardActions import \
    LocalCarStatusCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalDepositAmountCardActions import \
    LocalDepositAmountCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalDepositMaturityDateCardActions import \
    LocalDepositMaturityDateCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalDepositMonthlyPercentsCardActions import \
    LocalDepositMonthlyPercentsCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalFlatAreaCardActions import LocalFlatAreaCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalFlatStatusCardActions import \
    LocalFlatStatusCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalHouseAreaCardActions import \
    LocalHouseAreaCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalHouseStatusCardActions import \
    LocalHouseStatusCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.actions.LocalOtherAssetsPriceCardActions import \
    LocalOtherAssetsPriceCardActions
from core.scoring.apps.local.scoring_cards.assets_cards.plain_models import LocalAvailableAssetsCardPlainModel, \
    LocalFlatStatusCardPlainModel, LocalHouseStatusCardPlainModel, LocalCarStatusCardPlainModel
from core.scoring.apps.local.services.LocalAssetsScoringService import LocalAssetsScoringService
from django.utils.translation import ugettext_lazy as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class AssetScoringModule(BaseScoringModule):
    assets_service = LocalAssetsScoringService()
    available_actions = LocalAvailableAssetsScoringCardActions()
    car_lifetime_actions = LocalCarLifetimeCardActions()
    car_mileage_actions = LocalCarMileageCardActions()
    car_status_actions = LocalCarStatusCardActions()
    deposit_amount_actions = LocalDepositAmountCardActions()
    deposit_maturity_actions = LocalDepositMaturityDateCardActions()
    deposit_percents_actions = LocalDepositMonthlyPercentsCardActions()
    flat_area_actions = LocalFlatAreaCardActions()
    flat_status_actions = LocalFlatStatusCardActions()
    house_area_actions = LocalHouseAreaCardActions()
    house_status_actions = LocalHouseStatusCardActions()
    other_assets_actions = LocalOtherAssetsPriceCardActions()

    def calculate_score(self, data):
        # if available_assets_score == self.available_actions.get_max_score():
        if self.check_available_assets(data):
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
        else:
            data = LocalAssetsScoringPlainModel(
                # available_assets_score=available_assets_score,
                # total_score=available_assets_score,
                available_assets_score=0,
                total_score=0,
            )
        assets_data = self.assets_service.create(data)
        return assets_data

    @staticmethod
    def check_available_assets(data):
        result = 0
        for field in AssetsPlainModel().fields:
            if hasattr(data.profile_assets, field):
                result += 1
        return True if result else False

    def calculate_available_assets_score(self, data):
        score = self.available_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_available_assets'):
            data = LocalAvailableAssetsCardPlainModel(key=int(getattr(data.profile_assets, 'assets_available_assets')))
            score = self.available_actions.service.get_item(**data.__dict__).value if \
                self.available_actions.service.get_item(**data.__dict__) else self.available_actions.get_min_score()
        return score

    def calculate_other_assets_price_score(self, data):
        score = self.other_assets_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_other_assets_price'):
            price = float(getattr(data.profile_assets, 'assets_other_assets_price'))
            if price >= float(self.other_assets_actions.get_max_key()):
                score = self.other_assets_actions.get_max_score()
            else:
                for item in self.other_assets_actions.get_card():
                    if price < float(item.key):
                        score = item.value
                        break
        return score

    def calculate_flat_score(self, data):
        area_score = self._calculate_flat_area_score(data)
        print 'flat area score: %s' % area_score
        status_score = self._calculate_flat_status_score(data)
        print 'flat status score: %s' % status_score
        total_score = area_score + status_score
        data = LocalAssetsScoringPlainModel(flat_score=total_score, flat_area_score=area_score,
                                            flat_status_score=status_score, )
        return data

    def _calculate_flat_area_score(self, data):
        score = self.flat_area_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_flat_area'):
            flat_area = getattr(data.profile_assets, 'assets_flat_area')
            if flat_area >= float(self.flat_area_actions.get_max_key()):
                score = self.flat_area_actions.get_max_score()
            else:
                for item in self.flat_area_actions.get_card():
                    if flat_area < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_flat_status_score(self, data):
        score = self.flat_status_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_flat_state'):
            data = LocalFlatStatusCardPlainModel(key=int(getattr(data.profile_assets, 'assets_flat_state')))
            score = self.flat_status_actions.service.get_item(**data.__dict__).value if \
                self.flat_status_actions.service.get_item(**data.__dict__) else self.flat_status_actions.get_min_score()
        return score

    def calculate_house_score(self, data):
        area_score = self._calculate_house_area_score(data)
        print 'house area score: %s' % area_score
        status_score = self._calculate_house_status_score(data)
        print 'house status score: %s' % status_score
        total_score = area_score + status_score
        data = LocalAssetsScoringPlainModel(
            house_score=total_score,
            house_area_score=area_score,
            house_status_score=status_score,
        )
        return data

    def _calculate_house_area_score(self, data):
        score = self.house_area_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_house_area'):
            house_area = getattr(data.profile_assets, 'assets_house_area')
            if house_area >= float(self.house_area_actions.get_max_key()):
                score = self.house_area_actions.get_max_score()
            else:
                for item in self.house_area_actions.get_card():
                    if house_area < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_house_status_score(self, data):
        score = self.house_status_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_house_state'):
            data = LocalHouseStatusCardPlainModel(key=int(getattr(data.profile_assets, 'assets_house_state')))
            score = self.house_status_actions.service.get_item(**data.__dict__).value if \
                self.house_status_actions.service.get_item(**data.__dict__) else \
                self.house_status_actions.get_min_score()
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
        score = self.car_status_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_car_state'):
            data = LocalCarStatusCardPlainModel(key=int(getattr(data.profile_assets, 'assets_car_state')))
            score = self.car_status_actions.service.get_item(**data.__dict__).value if \
                self.car_status_actions.service.get_item(**data.__dict__) else self.car_status_actions.get_min_score()
        return score

    def _calculate_car_year_manufacture_score(self, data):
        score = self.car_lifetime_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_car_year_manufacture'):
            car_year = int(getattr(data.profile_assets, 'assets_car_year_manufacture'))
            current_year = datetime.datetime.today().year
            year = abs(current_year - car_year)
            if year >= self.car_lifetime_actions.get_max_key():
                score = self.car_lifetime_actions.get_max_score()
            else:
                for item in self.car_lifetime_actions.get_card(reverse=True):
                    if int(year) < int(item.key):
                        score = item.value
                        break
        return score

    def _calculate_car_mileage_score(self, data):
        score = self.car_mileage_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_car_mileage'):
            mileage = int(getattr(data.profile_assets, 'assets_car_mileage'))
            if int(mileage) >= self.car_mileage_actions.get_max_key():
                score = self.car_mileage_actions.get_max_score()
            else:
                for item in self.car_mileage_actions.get_card(reverse=True):
                    if int(mileage) < int(item.key):
                        score = item.value
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
        score = self.deposit_amount_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_deposits_amount'):
            amount = float(getattr(data.profile_assets, 'assets_deposits_amount'))
            if amount >= float(self.deposit_amount_actions.get_max_key()):
                score = self.deposit_amount_actions.get_max_score()
            else:
                for item in self.deposit_amount_actions.get_card():
                    if amount < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_deposits_monthly_percents_score(self, data):
        score = self.deposit_percents_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_deposits_monthly_percents'):
            percents = float(getattr(data.profile_assets, 'assets_deposits_monthly_percents'))
            if percents >= float(self.deposit_percents_actions.get_max_key()):
                score = self.deposit_percents_actions.get_max_score()
            else:
                for item in self.deposit_percents_actions.get_card():
                    if percents < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_deposits_maturity_date_score(self, data):
        score = self.deposit_maturity_actions.get_min_score()
        if hasattr(data.profile_assets, 'assets_deposits_maturity_date'):
            maturity_date = datetime.datetime.strptime(
                getattr(data.profile_assets, 'assets_deposits_maturity_date'), BASE_DATE_FORMAT)
            current_date = datetime.datetime.now()
            days = abs(maturity_date - current_date).days
            months = int(days / 30)
            if months >= self.deposit_maturity_actions.get_max_key():
                score = self.deposit_maturity_actions.get_max_score()
            else:
                for item in self.deposit_maturity_actions.get_card():
                    if months < item.key:
                        score = item.value
                        break
        return score