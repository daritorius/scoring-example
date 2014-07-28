# -*- coding: utf-8 -*-
import json
from django import http
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from web.scoring.main.facades.IndexFacade import IndexFacade
from web.scoring.main.forms.IndexForm import IndexForm


class IndexView(FormView):
    template_name = 'scoring/main/index.html'
    form_class = IndexForm
    index_facade = IndexFacade()

    def form_valid(self, form):
        score = self.index_facade.calculate_scoring(form.cleaned_data, self.request)
        result = {'result': True, 'score': score}
        return http.HttpResponse(json.dumps(result), content_type='application/json')

    def form_invalid(self, form):
        result = {'result': False, 'errors': [(k, [v[0], form.fields[k].label]) for k, v in form.errors.items()]}
        return http.HttpResponse(json.dumps(result), content_type='application/json')