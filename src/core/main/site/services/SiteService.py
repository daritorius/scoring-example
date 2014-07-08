#-*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from django.utils.translation import ugettext as _
from django.conf import settings


class PlainSiteObject(object):
    __metaclass__ = Singleton

    def __init__(self, domain):
        self.domain = domain
        self.name = domain


class SiteService(object):
    __metaclass__ = Singleton

    site = settings.CURRENT_SITE
    local_domains = ['127.0.0.1:8000', 'localhost:8000', 'sandbox.mybrains.org', 'example.com', 'mybrains.loc',
                     'sandbox.mybrains.ru']

    def get_current(self):
        site_object = PlainSiteObject(self.site)
        if self.site in self.local_domains:
            site_object.full = 'http://' + self.site
        else:
            site_object.full = 'https://' + self.site
        return site_object