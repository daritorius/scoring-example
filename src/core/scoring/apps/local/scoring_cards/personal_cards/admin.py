# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.personal_cards.models import LocalPersonalEducationCard, \
    LocalPersonalMaritalStatusNormalCard, LocalPersonalMaritalStatusBadCard, LocalPersonalIdentityAddressesCard
from django.contrib import admin
from django.utils.translation import ugettext as _


admin.site.register(LocalPersonalEducationCard)
admin.site.register(LocalPersonalMaritalStatusNormalCard)
admin.site.register(LocalPersonalMaritalStatusBadCard)
admin.site.register(LocalPersonalIdentityAddressesCard)