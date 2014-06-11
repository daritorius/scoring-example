#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.scoring.services.ScoringService import ScoringService
from django.conf.global_settings import DEBUG, DEFAULT_FROM_EMAIL
import os
from source.settings.apps_settings import REPORTS_MANAGER
import xlwt
from datetime import date
from django.core.mail import EmailMessage
from django.core.management import BaseCommand


class Command(BaseCommand):
    path_to_report = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../reports/'))
    scoring_service = ScoringService()

    def handle(self, *args, **options):
        print u'Получаем список элементов'
        scorings = self.scoring_service.get_all()

        print u'Генерируем отчет'
        font1 = xlwt.Font()
        font1.name = 'Times New Roman'
        font1.colour_index = 2
        font1.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font1

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(u'Отчет')

        ws.col(0).width = 1000
        for number in range(1, 51):
            ws.col(number).width = 10000

        ws.write(0, 0, u'№')
        ws.write(0, 1, u'A1')
        ws.write(0, 2, u'Дата рождения')
        ws.write(0, 3, u'Возраст')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A2')
        ws.write(0, 2, u'Образование')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A3')
        ws.write(0, 2, u'Семейное положение')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A4')
        ws.write(0, 2, u'Иждивенцы (в т.ч. неработающие члены семьи и дети до 21)')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A5')
        ws.write(0, 2, u'Место регистрации')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A6')
        ws.write(0, 2, u'Место проживания')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 1, u'A7')
        ws.write(0, 2, u'Совпадение места проживания и регистрации')
        ws.write(0, 4, u'Баллы по секции')

        ws.write(0, 5, u'B1')
        ws.write(0, 6, u'Тип трудоустройства')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B2')
        ws.write(0, 6, u'Стаж работы на текущем месте работы')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B3')
        ws.write(0, 6, u'Размер заработной платы')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B4')
        ws.write(0, 6, u'Должность')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B5')
        ws.write(0, 6, u'Рейтинг предприятия')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B6')
        ws.write(0, 6, u'стаж работы в качестве ЧП или количество лет работающего собственного предприятия')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B7')
        ws.write(0, 6, u'сумма уплаченного налога на прибыль (единого налога) за последний отчетный период')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 5, u'B8')
        ws.write(0, 6, u'количество сотрудников, работающих по найму')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 8, u'C1')
        ws.write(0, 9, u'Среднемесячные доходы (включая основные и дополнительные доходы)')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2')
        ws.write(0, 9, u'Наличие непогашенного кредита/займа')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2.1')
        ws.write(0, 9, u'Сумма кредита/займа')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2.2')
        ws.write(0, 9, u'Процент (доля) погашенной части кредита')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2.3')
        ws.write(0, 9, u'Количество дней до плановой даты погашения кредита')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2.4')
        ws.write(0, 9, u'Ежемесячный платеж')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 8, u'C2.5')
        ws.write(0, 9, u'Долговая нагрузка')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 11, u'C3')
        ws.write(0, 12, u'Среднемесячный остаток свободных денежных средств (доходы минус расходы)')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D1')
        ws.write(0, 12, u'Наличие активов')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D2')
        ws.write(0, 12, u'общая площадь квартиры')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D3')
        ws.write(0, 12, u'состояние квартиры')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D4')
        ws.write(0, 12, u'рейтинг района квартиры')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D5')
        ws.write(0, 12, u'общая площадь дома')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D6')
        ws.write(0, 12, u'состояние дома')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D7')
        ws.write(0, 12, u'рейтинг района дома')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D8')
        ws.write(0, 12, u'год эксплуатации автомобиля')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D9')
        ws.write(0, 12, u'пробег автомобиля')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D10')
        ws.write(0, 12, u'состояние автомобиля')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D11')
        ws.write(0, 12, u'срок окончания депозита')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D12')
        ws.write(0, 12, u'сумма депозита')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D13')
        ws.write(0, 12, u'ежемесячные выплаты процентов')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 11, u'D14')
        ws.write(0, 12, u'текущая оценочная стоимость активов')
        ws.write(0, 13, u'Баллы по секции')

        for number, item in enumerate(scorings, start=1):
            print number, item

        # for number, user in enumerate(users, start=1):
        #         ws.write(number, 0, number)
        #         ws.write(number, 1, u'%s' % profile.get_gender())
        #         ws.write(number, 2, u'%s' % profile.citizenship.title if profile.citizenship else '')

        # print u'Сохраняем отчет'
        # file_name = '/report_borrowers_%s.xls' % date.today()
        # path_to_file = self.path_to_report + file_name
        # wb.save(path_to_file)
        #
        # print u'Отправляем письма с отчетом'
        # ## send email to managers
        # from_email = DEFAULT_FROM_EMAIL
        # subject = u"[simzirok.com] Отчет о заемщиках в системе"
        # body = u"Добрый день! \n Отчет во вложении"
        #
        # receivers = REPORTS_MANAGER
        # print u'Получатели: %s' % receivers
        # print u'DEBUG: %s' % DEBUG
        # msg = EmailMessage(subject, body, from_email, receivers)
        # msg.attach_file(path_to_file, 'application/xls')
        # msg.content_subtype = "html"
        # msg.send()
        # print u'Сообщение отправлено'