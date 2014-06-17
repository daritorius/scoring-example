# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.credit_cards.models import LocalDependentsCard, LocalDebtBurdenLoansCard, \
    LocalMonthlyPaymentLoansCard, LocalDaysRepaymentLoansCard, LocalPercentRepaymentLoansCard, LocalAmountLoansCard, \
    LocalOutstandingLoansCard
from django.contrib import admin
from django.utils.translation import ugettext as _


admin.site.register(LocalOutstandingLoansCard)
admin.site.register(LocalAmountLoansCard)
admin.site.register(LocalPercentRepaymentLoansCard)
admin.site.register(LocalDaysRepaymentLoansCard)
admin.site.register(LocalMonthlyPaymentLoansCard)
admin.site.register(LocalDebtBurdenLoansCard)
admin.site.register(LocalDependentsCard)