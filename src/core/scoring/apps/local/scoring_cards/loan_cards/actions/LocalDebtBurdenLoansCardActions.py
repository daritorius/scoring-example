# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.services.LocalDebtBurdenLoansCardService import \
    LocalDebtBurdenLoansCardService
from django.utils.translation import ugettext as _


class LocalDebtBurdenLoansCardActions(BaseScoringCardActions):
    service = LocalDebtBurdenLoansCardService()