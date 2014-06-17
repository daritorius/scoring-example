# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class LocalPlacementTypeCard(BaseScoringCardModel):
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

    BaseScoringCardModel.key = models.IntegerField(_(u'Значение'), default=TYPE_UNEMPLOYED, choices=PLACEMENT_TYPES,
                                                   max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementTypeCardService import \
            LocalPlacementTypeCardService

        service = LocalPlacementTypeCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_type_card'
        verbose_name = _(u'Local placement type card')
        verbose_name_plural = _(u'Local placement type cards')


class LocalPlacementIncomeCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.placement_cards.services.LocalPlacementTypeCardService import \
            LocalPlacementTypeCardService

        service = LocalPlacementTypeCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_income_card'
        verbose_name = _(u'Local placement income card')
        verbose_name_plural = _(u'Local placement income cards')