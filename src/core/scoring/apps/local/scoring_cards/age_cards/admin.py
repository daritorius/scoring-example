# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.scoring.apps.local.scoring_cards.age_cards.models import LocalAgeScoringCard
from django.contrib import admin


admin.site.register(LocalAgeScoringCard)