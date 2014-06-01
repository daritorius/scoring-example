# -*- coding: utf-8 -*-
import json
from django import http
from django.utils.translation import ugettext_lazy as _
from api.facades.LocalScoringFacade import LocalScoringFacade
from django.views.generic import View


class LocalScoringView(View):
    local_scoring_facade = LocalScoringFacade()

    def get(self, request, *args, **kwargs):
        result = self.local_scoring_facade.process_request(request.GET)
        return http.HttpResponse(json.dumps({'result': result}), content_type='application/json')