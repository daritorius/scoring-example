# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class LocalOutstandingLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LoanOutstandingLoansCardService import \
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
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalAmountLoansCardService import \
            LocalAmountLoansCardService

        service = LocalAmountLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_amount_card'
        verbose_name = _(u'Local loan amount card')
        verbose_name_plural = _(u'Local loan amount cards')


class LocalPercentRepaymentLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalPercentRepaymentLoansCardService import \
            LocalPercentRepaymentLoansCardService

        service = LocalPercentRepaymentLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_repayment_percent_card'
        verbose_name = _(u'Local loan repayment % card')
        verbose_name_plural = _(u'Local loan repayment % cards')


class LocalDaysRepaymentLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDaysRepaymentLoansCardService import \
            LocalDaysRepaymentLoansCardService

        service = LocalDaysRepaymentLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_days_repayment_card'
        verbose_name = _(u'Local loan days to repayment card')
        verbose_name_plural = _(u'Local loan days to repayment cards')


class LocalMonthlyPaymentLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalMonthlyPaymentLoansCardService import \
            LocalMonthlyPaymentLoansCardService

        service = LocalMonthlyPaymentLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_monthly_payment_card'
        verbose_name = _(u'Local loan monthly payment card')
        verbose_name_plural = _(u'Local loan monthly payment cards')


class LocalDebtBurdenLoansCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDebtBurdenLoansCardService import \
            LocalDebtBurdenLoansCardService

        service = LocalDebtBurdenLoansCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_debt_burden_card'
        verbose_name = _(u'Local loan debt burden card')
        verbose_name_plural = _(u'Local loan debt burden cards')


class LocalDependentsCard(BaseScoringCardModel):
    NO_DEPENDENTS = 0
    ONE_DEPENDENT = 1
    TWO_DEPENDENTS = 2
    THREE_DEPENDENTS = 3
    FOUR_DEPENDENTS = 4
    MORE_THAN_4_DEPENDENTS = 5

    COUNT_DEPENDENTS = (
        (NO_DEPENDENTS, _(u'Ну ваще нету')),
        (ONE_DEPENDENT, _(u'Один какой-то там был')),
        (TWO_DEPENDENTS, _(u'Уже два о_О')),
        (THREE_DEPENDENTS, _(u'Начиная с трех можно дальше не считать')),
        (FOUR_DEPENDENTS, _(u'Уже четыре')),
        (MORE_THAN_4_DEPENDENTS, _(u'Пофиг уже, 4 и более')),
    )

    BaseScoringCardModel.key = models.IntegerField(_(u'Баллы'), default=NO_DEPENDENTS, choices=COUNT_DEPENDENTS,
                                                   max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDependentsCardService import \
            LocalDependentsCardService

        service = LocalDependentsCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_dependents_card'
        verbose_name = _(u'Local dependents card')
        verbose_name_plural = _(u'Local dependents cards')