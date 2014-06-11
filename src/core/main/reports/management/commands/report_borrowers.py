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

        ws.write(0, 5, u'A2')
        ws.write(0, 6, u'Образование')
        ws.write(0, 7, u'Баллы по секции')

        ws.write(0, 8, u'A3')
        ws.write(0, 9, u'Семейное положение')
        ws.write(0, 10, u'Баллы по секции')

        ws.write(0, 11, u'A4')
        ws.write(0, 12, u'Иждивенцы (в т.ч. неработающие члены семьи и дети до 21)')
        ws.write(0, 13, u'Баллы по секции')

        ws.write(0, 14, u'A5')
        ws.write(0, 15, u'Место регистрации')
        ws.write(0, 16, u'Баллы по секции')

        ws.write(0, 17, u'A6')
        ws.write(0, 18, u'Место проживания')
        ws.write(0, 19, u'Баллы по секции')

        ws.write(0, 20, u'A7')
        ws.write(0, 21, u'Совпадение места проживания и регистрации')
        ws.write(0, 22, u'Баллы по секции')

        ws.write(0, 23, u'B1')
        ws.write(0, 24, u'Тип трудоустройства')
        ws.write(0, 25, u'Баллы по секции')

        ws.write(0, 26, u'B2')
        ws.write(0, 27, u'Стаж работы на текущем месте работы')
        ws.write(0, 28, u'Баллы по секции')

        ws.write(0, 29, u'B3')
        ws.write(0, 30, u'Размер заработной платы')
        ws.write(0, 31, u'Баллы по секции')

        ws.write(0, 32, u'B4')
        ws.write(0, 33, u'Должность')
        ws.write(0, 34, u'Баллы по секции')

        ws.write(0, 35, u'B5')
        ws.write(0, 36, u'Рейтинг предприятия')
        ws.write(0, 37, u'Баллы по секции')

        ws.write(0, 38, u'B6')
        ws.write(0, 39, u'стаж работы в качестве ЧП или количество лет работающего собственного предприятия')
        ws.write(0, 40, u'Баллы по секции')

        ws.write(0, 41, u'B7')
        ws.write(0, 42, u'сумма уплаченного налога на прибыль (единого налога) за последний отчетный период')
        ws.write(0, 43, u'Баллы по секции')

        ws.write(0, 44, u'B8')
        ws.write(0, 45, u'количество сотрудников, работающих по найму')
        ws.write(0, 46, u'Баллы по секции')

        ws.write(0, 47, u'C1')
        ws.write(0, 48, u'Среднемесячные доходы (включая основные и дополнительные доходы)')
        ws.write(0, 49, u'Баллы по секции')

        ws.write(0, 50, u'C2')
        ws.write(0, 51, u'Наличие непогашенного кредита/займа')
        ws.write(0, 52, u'Баллы по секции')

        ws.write(0, 53, u'C2.1')
        ws.write(0, 54, u'Сумма кредита/займа')
        ws.write(0, 55, u'Баллы по секции')

        ws.write(0, 56, u'C2.2')
        ws.write(0, 57, u'Процент (доля) погашенной части кредита')
        ws.write(0, 58, u'Баллы по секции')

        ws.write(0, 59, u'C2.3')
        ws.write(0, 60, u'Количество дней до плановой даты погашения кредита')
        ws.write(0, 61, u'Баллы по секции')

        ws.write(0, 62, u'C2.4')
        ws.write(0, 63, u'Ежемесячный платеж')
        ws.write(0, 64, u'Баллы по секции')

        ws.write(0, 65, u'C2.5')
        ws.write(0, 66, u'Долговая нагрузка')
        ws.write(0, 67, u'Баллы по секции')

        ws.write(0, 68, u'C3')
        ws.write(0, 69, u'Среднемесячный остаток свободных денежных средств (доходы минус расходы)')
        ws.write(0, 70, u'Баллы по секции')

        ws.write(0, 71, u'D1')
        ws.write(0, 72, u'Наличие активов')
        ws.write(0, 73, u'Баллы по секции')

        ws.write(0, 74, u'D2')
        ws.write(0, 75, u'общая площадь квартиры')
        ws.write(0, 76, u'Баллы по секции')

        ws.write(0, 77, u'D3')
        ws.write(0, 78, u'состояние квартиры')
        ws.write(0, 79, u'Баллы по секции')

        ws.write(0, 80, u'D4')
        ws.write(0, 81, u'рейтинг района квартиры')
        ws.write(0, 82, u'Баллы по секции')

        ws.write(0, 83, u'D5')
        ws.write(0, 84, u'общая площадь дома')
        ws.write(0, 85, u'Баллы по секции')

        ws.write(0, 86, u'D6')
        ws.write(0, 87, u'состояние дома')
        ws.write(0, 88, u'Баллы по секции')

        ws.write(0, 89, u'D7')
        ws.write(0, 90, u'рейтинг района дома')
        ws.write(0, 91, u'Баллы по секции')

        ws.write(0, 92, u'D8')
        ws.write(0, 93, u'год эксплуатации автомобиля')
        ws.write(0, 94, u'Баллы по секции')

        ws.write(0, 95, u'D9')
        ws.write(0, 96, u'пробег автомобиля')
        ws.write(0, 97, u'Баллы по секции')

        ws.write(0, 98, u'D10')
        ws.write(0, 99, u'состояние автомобиля')
        ws.write(0, 100, u'Баллы по секции')

        ws.write(0, 101, u'D11')
        ws.write(0, 102, u'срок окончания депозита')
        ws.write(0, 103, u'Баллы по секции')

        ws.write(0, 104, u'D12')
        ws.write(0, 105, u'сумма депозита')
        ws.write(0, 106, u'Баллы по секции')

        ws.write(0, 107, u'D13')
        ws.write(0, 108, u'ежемесячные выплаты процентов')
        ws.write(0, 109, u'Баллы по секции')

        ws.write(0, 110, u'D14')
        ws.write(0, 111, u'текущая оценочная стоимость активов')
        ws.write(0, 112, u'Баллы по секции')

        ws.write(0, 113, u'Итоговый бал')

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