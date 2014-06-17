# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.credit_cards.models import LocalMonthlyPaymentLoansCard
from django.utils.translation import ugettext as _


class LocalMonthlyPaymentLoansCardService(BaseService):
    model_instance = LocalMonthlyPaymentLoansCard