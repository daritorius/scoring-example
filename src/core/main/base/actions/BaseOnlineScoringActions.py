# -*- coding: utf-8 -*-
import json
import urllib
import urllib2
from core.main.base.actions.BaseActions import BaseActions
from django.utils.translation import ugettext_lazy as _


class BaseOnlineScoringActions(BaseActions):
    url = None
    query = None
    base_path = ''
    format = 'json'
    port = 80
    method = 'GET'
    source = 'yandex'

    def check_address(self, data):
        self.check_official_address(data)
        self.check_real_address(data)

    def check_official_address(self, data):
        query = self.make_query(data, address_type='official')
        self.make_request(query)

    def check_real_address(self, data):
        query = self.make_query(data, address_type='real')
        self.make_request(query)

    @staticmethod
    def make_query(data, address_type='official'):
        query = ''
        if address_type == 'real':
            country = getattr(data.profile_real_address, '%s_country' % address_type) if \
                hasattr(data.profile_real_address, '%s_country' % address_type) else None
            city = getattr(data.profile_real_address, '%s_city' % address_type) if \
                hasattr(data.profile_real_address, '%s_city' % address_type) else None
            street = getattr(data.profile_real_address, '%s_street' % address_type) if \
                hasattr(data.profile_real_address, '%s_street' % address_type) else None
            house = getattr(data.profile_real_address, '%s_house' % address_type) if \
                hasattr(data.profile_real_address, '%s_house' % address_type) else None
        else:
            country = getattr(data.profile_official_address, '%s_country' % address_type) if \
                hasattr(data.profile_official_address, '%s_country' % address_type) else None
            city = getattr(data.profile_official_address, '%s_city' % address_type) if \
                hasattr(data.profile_official_address, '%s_city' % address_type) else None
            street = getattr(data.profile_official_address, '%s_street' % address_type) if \
                hasattr(data.profile_official_address, '%s_street' % address_type) else None
            house = getattr(data.profile_official_address, '%s_house' % address_type) if \
                hasattr(data.profile_official_address, '%s_house' % address_type) else None
        ## make query
        query += '%s' % country if country else ''
        if len(query) and city:
            query += ',+%s' % city
        elif not len(query) and city:
            query += '%s' % city
        if len(query) and street:
            query += ',+%s' % street
        elif not len(query) and street:
            query += '%s' % street
        if len(query) and house:
            query += ',+%s' % house
        elif not len(query) and house:
            query += '%s' % house
        return query

    def make_request(self, query):
        if self.source == 'google':
            query_data = {self.query: query, 'sensor': 'false'}
        else:
            query_data = {'geocode': query, 'format': self.format}
        geo_data = self.make_connection(query_data)
        try:
            if self.source == 'google':
                status = geo_data['status']
                if status == 'OK':
                    print 'found in geo google: %s' % status
            else:
                count = geo_data['response']['GeoObjectCollection']['metaDataProperty'][
                    'GeocoderResponseMetaData']['found']
                if count:
                    print 'found in geo yandex: %s' % count
        except Exception as e:
            print e

    def make_connection(self, data):
        try:
            if data is not None:
                data = urllib.urlencode(data)
            result = json.loads(urllib2.urlopen(self.url + self.base_path + '?' + data).read())
            return result
        except Exception as e:
            print 'Error: %s' % e
            return None