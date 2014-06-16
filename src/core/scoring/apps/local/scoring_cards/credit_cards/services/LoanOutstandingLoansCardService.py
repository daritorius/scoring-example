# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.credit_cards.models import LoanOutstandingLoansCard
from django.utils.translation import ugettext as _


class LoanOutstandingLoansCardService(BaseService):
    model_instance = LoanOutstandingLoansCard