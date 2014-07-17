# -*- coding: utf-8 -*-
import json
from api.facades.TotalScoringFacade import TotalScoringFacade
from django import http
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View


class TotalScoringView(View):
    total_scoring_facade = TotalScoringFacade()

    def get(self, request):
        result = self.total_scoring_facade.process_request(request.GET)
        # result = {'error': 'accept only post requests'}
        return http.HttpResponse(json.dumps(result), content_type='application/json')

    def post(self, request):
        try:
            result = self.total_scoring_facade.process_request(request.POST)
        except Exception as e:
            result = {'error': e}
        return http.HttpResponse(json.dumps(result), content_type='application/json')