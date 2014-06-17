# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.main.base.scoring.cards.BaseScoringCardPlainModel import BaseScoringCardPlainModel


class LocalAvailableAssetsCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalFlatAreaCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalFlatStatusCardPlainModel(BaseScoringCardPlainModel):
    fields = BaseScoringCardPlainModel.fields + ['status']


class LocalHouseAreaCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalHouseStatusCardPlainModel(BaseScoringCardPlainModel):
    fields = BaseScoringCardPlainModel.fields + ['status']


class LocalCarLifetimeCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalCarMileageCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalCarStatusCardPlainModel(BaseScoringCardPlainModel):
    fields = BaseScoringCardPlainModel.fields + ['status']


class LocalDepositMaturityDateCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalDepositAmountCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalDepositMonthlyPercentsCardPlainModel(BaseScoringCardPlainModel):
    pass


class LocalOtherAssetsPriceCardPlainModel(BaseScoringCardPlainModel):
    pass