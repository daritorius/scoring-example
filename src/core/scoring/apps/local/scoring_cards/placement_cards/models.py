# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class LocalPlacementTypeCard(BaseModel):
    TYPE_UNEMPLOYED = 0
    TYPE_HOUSEWIFE = 1
    TYPE_STUDENT = 2
    TYPE_PENSIONER = 3
    TYPE_SOLDIER = 4
    TYPE_WAGE_EARNER = 5
    TYPE_PRIVATE_ENTREPRENEUR = 6

    PLACEMENT_TYPES = (
        (TYPE_UNEMPLOYED, u'Безработный'),
        (TYPE_HOUSEWIFE, u'Домохозяйка'),
        (TYPE_STUDENT, u'Студент'),
        (TYPE_PENSIONER, u'Пенсионер'),
        (TYPE_SOLDIER, u'Военнослужащий'),
        (TYPE_WAGE_EARNER, u'Служащий'),
        (TYPE_PRIVATE_ENTREPRENEUR, u'Частный предприниматель'),
    )

    key = models.IntegerField(_(u'Значение'), default=TYPE_UNEMPLOYED, choices=PLACEMENT_TYPES, max_length=255,
                              blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementTypeCardService import \
            LocalPlacementTypeCardService

        service = LocalPlacementTypeCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_type_card'
        verbose_name = _(u'Local placement type card')
        verbose_name_plural = _(u'Local placement type')
        ordering = ['value']


class LocalPlacementIncomeCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementIncomeCardService import \
            LocalPlacementIncomeCardService

        service = LocalPlacementIncomeCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_income_card'
        verbose_name = _(u'Local placement income')
        verbose_name_plural = _(u'Local placement income')


class LocalPlacementCleanIncomeCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementCleanIncomeCardService import \
            LocalPlacementCleanIncomeCardService

        service = LocalPlacementCleanIncomeCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_clean_income_card'
        verbose_name = _(u'Local placement clean inc')
        verbose_name_plural = _(u'Local placement clean inc')


class LocalPlacementWageTermCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageTermCardService import \
            LocalPlacementWageTermCardService

        service = LocalPlacementWageTermCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_wage_term_card'
        verbose_name = _(u'Local placement wage term')
        verbose_name_plural = _(u'Local placement wage term')


class LocalPlacementWageEarnAmountCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageEarnAmountCardService import \
            LocalPlacementWageEarnAmountCardService

        service = LocalPlacementWageEarnAmountCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_wage_amount_card'
        verbose_name = _(u'Local placement wage amount')
        verbose_name_plural = _(u'Local placement wage amount')


class LocalPlacementWageCategoryCard(BaseModel):
    CATEGORY_SENIOR_MANAGER = 0
    CATEGORY_MIDDLE_MANAGER = 1
    CATEGORY_SPECIALIST = 2
    CATEGORY_JUNIOR_SPECIALIST = 3

    CATEGORIES = (
        (CATEGORY_SENIOR_MANAGER, _(u'Супер менеджер')),
        (CATEGORY_MIDDLE_MANAGER, _(u'Средний менеджер')),
        (CATEGORY_SPECIALIST, _(u'Просто менеджер')),
        (CATEGORY_JUNIOR_SPECIALIST, _(u'Мелкий менеджер')),
    )

    key = models.IntegerField(_(u'Значение'), choices=CATEGORIES, default=CATEGORY_JUNIOR_SPECIALIST, max_length=255,
                              blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementWageCategoryCardService import \
            LocalPlacementWageCategoryCardService

        service = LocalPlacementWageCategoryCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_wage_category_card'
        verbose_name = _(u'Local placement wage category')
        verbose_name_plural = _(u'Local placement wage category')
        ordering = ['value']


class LocalPlacementPeTermCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeTermCardService import \
            LocalPlacementPeTermCardService

        service = LocalPlacementPeTermCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_pe_term_card'
        verbose_name = _(u'Local placement pe term')
        verbose_name_plural = _(u'Local placement pe term ')


class LocalPlacementPeTaxCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeTaxCardService import \
            LocalPlacementPeTaxCardService

        service = LocalPlacementPeTaxCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_pe_tax_card'
        verbose_name = _(u'Local placement pe tax')
        verbose_name_plural = _(u'Local placement pe tax')


class LocalPlacementPeEmployeesCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementPeEmployeesCardService import \
            LocalPlacementPeEmployeesCardService

        service = LocalPlacementPeEmployeesCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_pe_employees_card'
        verbose_name = _(u'Local placement pe employees')
        verbose_name_plural = _(u'Local placement pe employees')