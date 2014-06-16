# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.utils.translation import ugettext as _


class LocalOutstandingLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.credit_cards.services.LoanOutstandingLoansCardService import \
            LoanOutstandingLoansCardService
        service = LoanOutstandingLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_available_card'
        verbose_name = _(u'Local loan available card')
        verbose_name_plural = _(u'Local loan available cards')


class LocalAmountLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.credit_cards.services.LocalAmountLoansCardService import \
            LocalAmountLoansCardService
        service = LocalAmountLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_amount_card'
        verbose_name = _(u'Local loan amount card')
        verbose_name_plural = _(u'Local loan amount cards')