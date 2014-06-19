# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.services.LoanOutstandingLoansCardService import \
    LoanOutstandingLoansCardService
from django.utils.translation import ugettext as _


class LoanOutstandingLoansCardActions(BaseScoringCardActions):
    service = LoanOutstandingLoansCardService()