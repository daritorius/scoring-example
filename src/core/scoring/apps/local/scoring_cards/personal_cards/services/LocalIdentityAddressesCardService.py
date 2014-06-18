# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.personal_cards.models import LocalPersonalIdentityAddressesCard
from django.utils.translation import ugettext as _


class LocalIdentityAddressesCardService(BaseService):
    model_instance = LocalPersonalIdentityAddressesCard