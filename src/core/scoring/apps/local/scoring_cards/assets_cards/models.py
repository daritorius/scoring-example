# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class BaseAssetStatusCard(models.Model):
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

    key = models.IntegerField(max_length=255, choices=STATES, default=REPAIR_STATE, blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    class Meta:
        abstract = True
        ordering = ['value']


class LocalAvailableAssetsCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalAssetsScoringCardService import \
            LocalAssetsScoringCardService
        service = LocalAssetsScoringCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_available_assets_card'
        verbose_name = _(u'Local available assets')
        verbose_name_plural = _(u'Local available assets')


class LocalFlatAreaCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatAreaCardService import \
            LocalFlatAreaCardService
        service = LocalFlatAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_flat_area_card'
        verbose_name = _(u'Local flat area')
        verbose_name_plural = _(u'Local flat area')


class LocalFlatStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalFlatAreaCardService import \
            LocalFlatAreaCardService
        service = LocalFlatAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_flat_status_card'
        verbose_name = _(u'Local flat status')
        verbose_name_plural = _(u'Local flat status')


class LocalHouseAreaCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseAreaCardService import \
            LocalHouseAreaCardService
        service = LocalHouseAreaCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_house_area_card'
        verbose_name = _(u'Local house area')
        verbose_name_plural = _(u'Local house area')


class LocalHouseStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalHouseStatusCardService import \
            LocalHouseStatusCardService
        service = LocalHouseStatusCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_house_status_card'
        verbose_name = _(u'Local house status')
        verbose_name_plural = _(u'Local house status')


class LocalCarLifetimeCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarLifetimeService import \
            LocalCarLifetimeService
        service = LocalCarLifetimeService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_lifetime_card'
        verbose_name = _(u'Local car lifetime')
        verbose_name_plural = _(u'Local car lifetime')


class LocalCarMileageCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarMileageCardService import \
            LocalCarMileageCardService
        service = LocalCarMileageCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_mileage_card'
        verbose_name = _(u'Local car mileage')
        verbose_name_plural = _(u'Local car mileage')


class LocalCarStatusCard(BaseAssetStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalCarStatusCardService import \
            LocalCarStatusCardService
        service = LocalCarStatusCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_car_status_card'
        verbose_name = _(u'Local car status')
        verbose_name_plural = _(u'Local car status')


class LocalDepositMaturityDateCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMaturityDateCardService import \
            LocalDepositMaturityDateCardService
        service = LocalDepositMaturityDateCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_maturity_card'
        verbose_name = _(u'Local deposit maturity')
        verbose_name_plural = _(u'Local deposit maturity')


class LocalDepositAmountCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositAmountCardService import \
            LocalDepositAmountCardService
        service = LocalDepositAmountCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_amount_card'
        verbose_name = _(u'Local deposit amount')
        verbose_name_plural = _(u'Local deposit amount')


class LocalDepositMonthlyPercentsCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalDepositMonthlyPercentsCardService import \
            LocalDepositMonthlyPercentsCardService
        service = LocalDepositMonthlyPercentsCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_deposit_percents_card'
        verbose_name = _(u'Local deposit percents')
        verbose_name_plural = _(u'Local deposit percents')


class LocalOtherAssetsPriceCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.assets_cards.services.LocalOtherAssetsPriceCardService import \
            LocalOtherAssetsPriceCardService
        service = LocalOtherAssetsPriceCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_other_assets_card'
        verbose_name = _(u'Local other assets')
        verbose_name_plural = _(u'Local other assets')