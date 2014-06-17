# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.loan_cards.models import LocalDaysRepaymentLoansCard
from django.utils.translation import ugettext as _


class LocalDaysRepaymentLoansCardService(BaseService):
    model_instance = LocalDaysRepaymentLoansCard