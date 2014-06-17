# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.loan_cards.models import LocalDebtBurdenLoansCard
from django.utils.translation import ugettext as _


class LocalDebtBurdenLoansCardService(BaseService):
    model_instance = LocalDebtBurdenLoansCard