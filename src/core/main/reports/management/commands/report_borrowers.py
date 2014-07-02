# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule
from core.scoring.apps.local.management.commands.plain_models.PersonalInformationCards import PersonalInformationCards
from core.scoring.apps.local.management.commands.plain_models.PlacementInformationCards import PlacementInformationCards
from core.scoring.apps.local.plain_models import ChargesPlainModel
from django.utils.translation import ugettext as _
from core.scoring.services.ScoringService import ScoringService
from django.conf.global_settings import DEBUG, DEFAULT_FROM_EMAIL
import os
from source.settings.apps_settings import REPORTS_MANAGER, BASE_DATE_FORMAT
import xlwt
import json
from django.core.mail import EmailMessage
from django.core.management import BaseCommand


class Command(BaseCommand):
    path_to_report = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../reports/'))
    scoring_service = ScoringService()
    age_module = AgeScoringModule()

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

        # ws.write(0, 71, u'D1')
        # ws.write(0, 72, u'Наличие активов')
        # ws.write(0, 73, u'Баллы по секции')
        #
        # ws.write(0, 74, u'D2')
        # ws.write(0, 75, u'общая площадь квартиры')
        # ws.write(0, 76, u'Баллы по секции')
        #
        # ws.write(0, 77, u'D3')
        # ws.write(0, 78, u'состояние квартиры')
        # ws.write(0, 79, u'Баллы по секции')
        #
        # ws.write(0, 80, u'D4')
        # ws.write(0, 81, u'рейтинг района квартиры')
        # ws.write(0, 82, u'Баллы по секции')
        #
        # ws.write(0, 83, u'D5')
        # ws.write(0, 84, u'общая площадь дома')
        # ws.write(0, 85, u'Баллы по секции')
        #
        # ws.write(0, 86, u'D6')
        # ws.write(0, 87, u'состояние дома')
        # ws.write(0, 88, u'Баллы по секции')
        #
        # ws.write(0, 89, u'D7')
        # ws.write(0, 90, u'рейтинг района дома')
        # ws.write(0, 91, u'Баллы по секции')
        #
        # ws.write(0, 92, u'D8')
        # ws.write(0, 93, u'год эксплуатации автомобиля')
        # ws.write(0, 94, u'Баллы по секции')
        #
        # ws.write(0, 95, u'D9')
        # ws.write(0, 96, u'пробег автомобиля')
        # ws.write(0, 97, u'Баллы по секции')
        #
        # ws.write(0, 98, u'D10')
        # ws.write(0, 99, u'состояние автомобиля')
        # ws.write(0, 100, u'Баллы по секции')
        #
        # ws.write(0, 101, u'D11')
        # ws.write(0, 102, u'срок окончания депозита')
        # ws.write(0, 103, u'Баллы по секции')
        #
        # ws.write(0, 104, u'D12')
        # ws.write(0, 105, u'сумма депозита')
        # ws.write(0, 106, u'Баллы по секции')
        #
        # ws.write(0, 107, u'D13')
        # ws.write(0, 108, u'ежемесячные выплаты процентов')
        # ws.write(0, 109, u'Баллы по секции')
        #
        # ws.write(0, 110, u'D14')
        # ws.write(0, 111, u'текущая оценочная стоимость активов')
        # ws.write(0, 112, u'Баллы по секции')

        ws.write(0, 71, u'Дата расчета')
        ws.write(0, 72, u'Итоговый бал')
        ws.write(0, 73, u'Рейтинг')

        for number, item in enumerate(scorings, start=1):
            user_data = json.loads(item.user_data)
            ws.write(number, 0, number)

            ws.write(number, 2, user_data.get('profile_birthday', u'Не указано'))
            age = self.age_module._get_age(
                datetime.datetime.strptime(user_data.get('profile_birthday'), BASE_DATE_FORMAT).date()) if \
                user_data.get('profile_birthday') else _(u'Не указано')
            ws.write(number, 3, age)
            ws.write(number, 4, item.local_score.age_score.total_score)

            personal_card = PersonalInformationCards()
            education = personal_card.EDUCATION_TYPES[str(user_data.get('personal_education'))] if \
                user_data.get('personal_education') != '' else _(u'Не указано')
            ws.write(number, 6, education)
            ws.write(number, 7, item.local_score.personal_score.education_score)

            marital_status = personal_card.MARITAL_STATUSES[str(user_data.get('personal_marital_status'))] if \
                user_data.get('personal_marital_status') != '' else _(u'Не указано')
            ws.write(number, 9, marital_status)
            ws.write(number, 10, item.local_score.personal_score.marital_status_score)

            dependents = user_data.get('personal_dependents', 0)
            ws.write(number, 12, dependents)
            ws.write(number, 13, item.local_score.loan_score.dependents_score)

            ws.write(number, 15, user_data.get('official_city'))
            ws.write(number, 16, item.local_score.personal_score.official_address_score)

            ws.write(number, 18, user_data.get('real_city'))
            ws.write(number, 19, item.local_score.personal_score.real_address_score)

            similar = user_data.get('profile_addresses_similar', _(u'Не указано'))
            if similar != '':
                similar = _(u'да') if int(similar) else _(u'нет')
            ws.write(number, 21, similar)
            ws.write(number, 22, item.local_score.personal_score.identity_addresses_score)

            placement_card = PlacementInformationCards()
            placement_type = placement_card.PLACEMENT_TYPES[str(user_data.get('placement_type'))] if \
                user_data.get('placement_type') != '' else _(u'Не указано')
            ws.write(number, 24, placement_type)
            ws.write(number, 25, item.local_score.placement_score.placement_type_score)

            ws.write(number, 36, u'Не учитывается')
            ws.write(number, 37, u'Не учитывается')

            if int(user_data.get('placement_type', None)) == placement_card.TYPE_WAGE_EARNER:
                placement_term = int(user_data.get('placement_term', 0)) * 12
                ws.write(number, 27, placement_term)
                ws.write(number, 28, item.local_score.placement_score.term_score)

                wage_total = str(user_data.get('placement_income', 0)) + ' + ' + \
                             str(user_data.get('placement_additional_income', 0))
                ws.write(number, 30, wage_total)
                ws.write(number, 31, item.local_score.placement_score.wage_score)

                position = placement_card.POSITION_CATEGORIES[str(user_data.get('placement_category_position', 0))]
                ws.write(number, 33, position)
                ws.write(number, 34, item.local_score.placement_score.category_position_score)
            elif int(user_data.get('placement_type', None)) == placement_card.TYPE_PRIVATE_ENTREPRENEUR:
                ws.write(number, 39, int(user_data.get('placement_term', 0)) * 12)
                ws.write(number, 40, item.local_score.placement_score.term_score)

                ws.write(number, 42, user_data.get('placement_tax_quarter', u'Не указано'))
                ws.write(number, 43, item.local_score.placement_score.tax_score)

                ws.write(number, 45, user_data.get('placement_organisation_count_employees', u'Не указано'))
                ws.write(number, 46, item.local_score.placement_score.count_employees_score)

                ws.write(number, 48, str(user_data.get('placement_income', 0)) + ' + ' + \
                         str(user_data.get('placement_additional_income', 0)))
                ws.write(number, 49, item.local_score.placement_score.placement_income_score)

            outstanding_loans = user_data.get('charges_outstanding_loans', '')
            if outstanding_loans != '':
                outstanding_loans = _(u'да') if int(outstanding_loans) else _(u'нет')

            if outstanding_loans != '' and not int(outstanding_loans):
                ws.write(number, 51, outstanding_loans)
                ws.write(number, 52, item.local_score.loan_score.outstanding_loan_score)

                ws.write(number, 54, user_data.get('charges_initial_amount', 0))
                ws.write(number, 55, item.local_score.loan_score.amount_loan_score)

                ws.write(number, 57, str(user_data.get('charges_initial_amount', 0)) + '/' +
                         str(user_data.get('charges_current_amount', 0)))
                ws.write(number, 58, item.local_score.loan_score.repayment_percent_score)

                ws.write(number, 60, user_data.get('charges_maturity_date', 0))
                ws.write(number, 61, item.local_score.loan_score.days_to_repayment_score)

                ws.write(number, 63, user_data.get('charges_monthly_payment', 0))
                ws.write(number, 64, item.local_score.loan_score.monthly_payment_score)

                payment = float(user_data.get('charges_monthly_payment', 0))
                income = float(user_data.get('placement_income', 0))
                try:
                    debt_burden = round(payment / income, 2)
                except ZeroDivisionError:
                    debt_burden = 1
                ws.write(number, 66, debt_burden)
                ws.write(number, 67, item.local_score.loan_score.debt_burden_score)

            income = float(user_data.get('placement_income', 0))
            add_income = float(user_data.get('placement_additional_income', 0))
            charges = 0
            for field in ChargesPlainModel().fields:
                charges += float(user_data.get(field, 0))
            clean_income = income + add_income - charges
            clean_string = u'( Доход: %s + Доп.доход: %s ) - Расходы: %s = Итого %s' % (income, add_income, charges,
                                                                                        clean_income)
            ws.write(number, 69, clean_string)
            ws.write(number, 70, item.local_score.placement_score.placement_clean_income)

            # ws.write(number, 72, user_data.get('assets_available_assets', u'Не указано'))
            # ws.write(number, 73, item.local_score.assets_score.available_assets_score)
            #
            # ws.write(number, 75, user_data.get('assets_flat_area', u'Не указано'))
            # ws.write(number, 76, item.local_score.assets_score.flat_area_score)
            #
            # ws.write(number, 78, user_data.get('assets_flat_state', u'Не указано'))
            # ws.write(number, 79, item.local_score.assets_score.flat_status_score)
            #
            # ws.write(number, 81, u'Не учитывается')
            # ws.write(number, 82, u'Не учитывается')
            #
            # ws.write(number, 84, user_data.get('assets_house_area', u'Не указано'))
            # ws.write(number, 85, item.local_score.assets_score.house_area_score)
            #
            # ws.write(number, 87, user_data.get('assets_house_state', u'Не указано'))
            # ws.write(number, 88, item.local_score.assets_score.house_status_score)
            #
            # ws.write(number, 90, u'Не учитывается')
            # ws.write(number, 91, u'Не учитывается')
            #
            # ws.write(number, 93, user_data.get('assets_car_year_manufacture', u'Не указано'))
            # ws.write(number, 94, item.local_score.assets_score.car_lifetime_score)
            #
            # ws.write(number, 96, user_data.get('assets_car_mileage', u'Не указано'))
            # ws.write(number, 97, item.local_score.assets_score.car_mileage_car_score)
            #
            # ws.write(number, 99, user_data.get('assets_car_state', u'Не указано'))
            # ws.write(number, 100, item.local_score.assets_score.car_status_score)
            #
            # ws.write(number, 102, user_data.get('assets_deposits_maturity_date', u'Не указано'))
            # ws.write(number, 103, item.local_score.assets_score.deposit_maturity_date_score)
            #
            # ws.write(number, 105, user_data.get('assets_deposits_amount', u'Не указано'))
            # ws.write(number, 106, item.local_score.assets_score.deposit_amount_score)
            #
            # ws.write(number, 108, user_data.get('assets_deposits_monthly_percents', u'Не указано'))
            # ws.write(number, 109, item.local_score.assets_score.deposit_percents_score)
            #
            # ws.write(number, 111, user_data.get('assets_other_assets_price', u'Не указано'))
            # ws.write(number, 112, item.local_score.assets_score.other_assets_score)

            ws.write(number, 71, item.date_create.strftime(BASE_DATE_FORMAT))
            ws.write(number, 72, item.local_score.total_score)
            ws.write(number, 73, item.local_score.rating)

        print u'Сохраняем отчет'
        file_name = '/report_scoring_%s.xls' % datetime.date.today()
        path_to_file = self.path_to_report + file_name
        wb.save(path_to_file)

        print u'Отправляем письма с отчетом'
        # # send email to managers
        from_email = DEFAULT_FROM_EMAIL
        subject = u"[simzirok.com] Отчет о заемщиках в системе"
        body = u"Добрый день! \n Отчет во вложении"

        receivers = REPORTS_MANAGER
        print u'Получатели: %s' % receivers
        print u'DEBUG: %s' % DEBUG
        msg = EmailMessage(subject, body, from_email, receivers)
        msg.attach_file(path_to_file, 'application/xls')
        msg.content_subtype = "html"
        msg.send()
        print u'Сообщение отправлено'