# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class BaseAssetStatusCard(BaseScoringCardModel):
    REPAIR_STATE = 0
    NORMAL_STATE = 1
    GOOD_STATE = 2
    BEST_STATE = 3

    STATES = (
        (REPAIR_STATE, _(u'Надо ремонтировать')),
        (NORMAL_STATE, _(u'Ну такое')),
        (GOOD_STATE, _(u'Вроде все нормик')),
        (BEST_STATE, _(u'Бест оф зи бест')),
    )

    status = models.IntegerField(max_length=255, choices=STATES, default=REPAIR_STATE)

    class Meta:
        abstract = True


class LocalAvailableAssetsCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalAssetsScoringCardService import \
            LocalAssetsScoringCardService
        service = LocalAssetsScoringCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_available_assets_card'
        verbose_name = _(u'Local available assets card')
        verbose_name_plural = _(u'Local available assets cards')


class LocalFlatAreaCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatAreaCardService import \
            LocalFlatAreaCardService
        service = LocalFlatAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_flat_area_card'
        verbose_name = _(u'Local flat area card')
        verbose_name_plural = _(u'Local flat area cards')


class LocalFlatStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatAreaCardService import \
            LocalFlatAreaCardService
        service = LocalFlatAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_flat_status_card'
        verbose_name = _(u'Local flat status card')
        verbose_name_plural = _(u'Local flat status cards')


class LocalHouseAreaCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseAreaCardService import \
            LocalHouseAreaCardService
        service = LocalHouseAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_house_area_card'
        verbose_name = _(u'Local house area card')
        verbose_name_plural = _(u'Local house area cards')


class LocalHouseStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseStatusCardService import \
            LocalHouseStatusCardService
        service = LocalHouseStatusCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_house_status_card'
        verbose_name = _(u'Local house status card')
        verbose_name_plural = _(u'Local house status cards')


class LocalCarLifetimeCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarLifetimeService import \
            LocalCarLifetimeService
        service = LocalCarLifetimeService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_lifetime_card'
        verbose_name = _(u'Local car lifetime card')
        verbose_name_plural = _(u'Local car lifetime cards')


class LocalCarMileageCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarMileageCardService import \
            LocalCarMileageCardService
        service = LocalCarMileageCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_mileage_card'
        verbose_name = _(u'Local car mileage card')
        verbose_name_plural = _(u'Local car mileage cards')


class LocalCarStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarStatusCardService import \
            LocalCarStatusCardService
        service = LocalCarStatusCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_status_card'
        verbose_name = _(u'Local car status card')
        verbose_name_plural = _(u'Local car status cards')


class LocalDepositMaturityDateCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMaturityDateCardService import \
            LocalDepositMaturityDateCardService
        service = LocalDepositMaturityDateCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_maturity_card'
        verbose_name = _(u'Local deposit maturity card')
        verbose_name_plural = _(u'Local deposit maturity cards')


class LocalDepositAmountCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositAmountCardService import \
            LocalDepositAmountCardService
        service = LocalDepositAmountCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_amount_card'
        verbose_name = _(u'Local deposit amount card')
        verbose_name_plural = _(u'Local deposit amount cards')


class LocalDepositMonthlyPercentsCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMonthlyPercentsCardService import \
            LocalDepositMonthlyPercentsCardService
        service = LocalDepositMonthlyPercentsCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_percents_card'
        verbose_name = _(u'Local deposit percents card')
        verbose_name_plural = _(u'Local deposit percents cards')


class LocalOtherAssetsPriceCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalOtherAssetsPriceCardService import \
            LocalOtherAssetsPriceCardService
        service = LocalOtherAssetsPriceCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_other_assets_card'
        verbose_name = _(u'Local other assets card')
        verbose_name_plural = _(u'Local other assets cards')