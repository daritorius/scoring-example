# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'scoring/main/index.html'