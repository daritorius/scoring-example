# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalAmountLoansCardService import \
    LocalAmountLoansCardService
from django.utils.translation import ugettext as _


class LocalAmountLoansCardActions(BaseScoringCardActions):
    service = LocalAmountLoansCardService()