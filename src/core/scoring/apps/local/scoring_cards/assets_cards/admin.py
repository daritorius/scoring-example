# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.assets_cards.models import LocalAvailableAssetsCard, \
    LocalOtherAssetsPriceCard, LocalDepositMonthlyPercentsCard, LocalDepositAmountCard, LocalDepositMaturityDateCard, \
    LocalCarStatusCard, LocalCarMileageCard, LocalCarLifetimeCard, LocalHouseStatusCard, LocalHouseAreaCard, \
    LocalFlatStatusCard, LocalFlatAreaCard
from django.contrib import admin
from django.utils.translation import ugettext as _


admin.site.register(LocalAvailableAssetsCard)
admin.site.register(LocalFlatAreaCard)
admin.site.register(LocalFlatStatusCard)
admin.site.register(LocalHouseAreaCard)
admin.site.register(LocalHouseStatusCard)
admin.site.register(LocalCarLifetimeCard)
admin.site.register(LocalCarMileageCard)
admin.site.register(LocalCarStatusCard)
admin.site.register(LocalDepositMaturityDateCard)
admin.site.register(LocalDepositAmountCard)
admin.site.register(LocalDepositMonthlyPercentsCard)
admin.site.register(LocalOtherAssetsPriceCard)