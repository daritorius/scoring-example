# -*- coding: utf-8 -*-
import json
from django import http
from django.utils.translation import ugettext_lazy as _
from api.facades.LocalScoringFacade import LocalScoringFacade
from django.views.generic import View


class LocalScoringView(View):
    local_scoring_facade = LocalScoringFacade()

    def get(self, request):
        # result = self.local_scoring_facade.process_request(request.GET)
        result = {'error': 'accept only post requests'}
        return http.HttpResponse(json.dumps(result), content_type='application/json')

    def post(self, request):
        try:
            result = self.local_scoring_facade.process_request(request.POST)
        except Exception as e:
            result = {'error': e}
        return http.HttpResponse(json.dumps(result), content_type='application/json')