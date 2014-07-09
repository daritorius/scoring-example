# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import datetime
from core.main.base.actions.BaseOnlineScoringActions import BaseOnlineScoringActions
import re
import urllib2
from bs4 import BeautifulSoup
from source.settings.apps_settings import BASE_DATE_FORMAT


class BasePersonsActions(BaseOnlineScoringActions):

    def check_person(self, data):
        query = self.make_query(data)
        result = self.make_connection(query)
        print 'person not found' if not len(result) else 'person found'

    @staticmethod
    def make_query(data):
        query = ''
        first_name = getattr(data, 'profile_first_name') if \
            hasattr(data, 'profile_first_name') else None
        third_name = getattr(data, 'profile_third_name') if \
            hasattr(data, 'profile_third_name') else None
        second_name = getattr(data, 'profile_second_name') if \
            hasattr(data, 'profile_second_name') else None
        birthday = getattr(data, 'profile_birthday') if \
            hasattr(data, 'profile_birthday') else None
        if birthday:
            birthday = '%s.%s.%s' % (
                str(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).day),
                str(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).month),
                str(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).year))

        query_data = {
            'FIRST_NAME': first_name,
            'LAST_NAME': third_name,
            'MIDDLE_NAME': second_name,
            'BIRTH_DATE_START': birthday,
            'BIRTH_DATE_END': birthday,
        }
        for key, value in query_data.iteritems():
            query += '%s=%s&' % (key, value)
        return query

    def make_connection(self, data):
        try:
            result = urllib2.urlopen(self.url + self.base_path + '?' + data).read()
            soup = BeautifulSoup(''.join(result))
            content = soup.findAll('a', {'class': re.compile(r'\bcontent\b')})
            return content
        except Exception as e:
            print 'Error while connect to database: %s' % e
            return None