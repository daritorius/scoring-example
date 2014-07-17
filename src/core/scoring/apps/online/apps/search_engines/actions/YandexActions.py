# -*- coding: utf-8 -*-
import datetime
import urllib
import re
import urllib2
from bs4 import BeautifulSoup
from core.main.base.actions.BaseActions import BaseActions
from django.utils.translation import ugettext_lazy as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class SearchYandexActions(BaseActions):
    url = 'http://yandex.ru/yandsearch?'
    query = 'text='

    def check_personal_information(self, data):
        pass

    def check_simple_search(self, data):
        # (Ф && Д1) | (Ф && Д2)
        user_data = self.make_data(data, full=False)
        print user_data
        # result = self.make_connection(user_data)
        # print result

    def check_vk(self, data):
        pass

    @staticmethod
    def make_data(data, full=True):
        first_name = getattr(data, 'profile_first_name') if \
            hasattr(data, 'profile_first_name') else None
        third_name = getattr(data, 'profile_third_name') if \
            hasattr(data, 'profile_third_name') else None
        second_name = getattr(data, 'profile_second_name') if \
            hasattr(data, 'profile_second_name') else None
        birthday = getattr(data, 'profile_birthday') if \
            hasattr(data, 'profile_birthday') else None

        day_birth = int(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).day)
        month_birth = int(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).month)
        year_birth = int(datetime.datetime.strptime(birthday, BASE_DATE_FORMAT).year)

        if birthday:
            birthday = '%s.%s.%s' % (day_birth, month_birth, year_birth)

        if full:
            user_data = {
                'first_name': first_name,
                'last_name': third_name,
                'middle_name': second_name,
                'birthday': birthday,
                'day_birth': day_birth,
                'month_birth': month_birth,
                'year_birth': year_birth,
            }
        else:
            user_data = {
                'first_name': first_name,
                'last_name': third_name,
                'middle_name': second_name,
                'birthday': birthday,
            }
        user_data = {'dict': user_data, 'query': urllib.urlencode(user_data)}
        return user_data

    def make_connection(self, data):
        try:
            result = urllib2.urlopen(self.url + self.query + data + '&lr=143').read()
            soup = BeautifulSoup(''.join(result))
            content = soup.findAll('a', {'class': re.compile(r'\bserp-item__title-link\b')})
            return content
        except Exception as e:
            print 'Error while connect to database: %s' % e
            return None