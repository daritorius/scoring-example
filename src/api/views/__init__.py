# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from api.views.LocalScoringView import LocalScoringView
from api.views.PlainView import PlainView
from api.views.TotalScoringView import TotalScoringView


plain_view = PlainView.as_view()
local_scoring_view = LocalScoringView.as_view()
total_scoring_view = TotalScoringView.as_view()