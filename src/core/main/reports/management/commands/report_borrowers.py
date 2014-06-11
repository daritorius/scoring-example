#-*- coding: utf-8 -*-
from core.scoring.services.ScoringService import ScoringService
from django.utils.translation import ugettext as _
from django.conf.global_settings import DEBUG, DEFAULT_FROM_EMAIL
import os
from source.settings.apps_settings import REPORTS_MANAGER
import xlwt
from datetime import date
from django.core.mail import EmailMessage
from django.core.management import BaseCommand


class Command(BaseCommand):
    path_to_report = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../reports/'))
    # report_service = ReportService()
    # user_profile_service = ProfileService()
    # scoring_service = ScoringService()
    scoring_service = ScoringService()

    def handle(self, *args, **options):
        print u'Получаем список пользователей'
        users_profiles = self.user_profile_service.get_all_borrowers_in_system().order_by('date_create')
        users = [item.user for item in users_profiles if item.form_page == 9]

        print u'Генерируем отчет'
        font1 = xlwt.Font()
        font1.name = 'Times New Roman'
        font1.colour_index = 2
        font1.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font1

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(u'Отчет о заемщиках в системе')

        ws.col(0).width = 1000
        for number in range(1, 51):
            ws.col(number).width = 10000

        ws.write(0, 0, u'№')
        ws.write(0, 3, u'Дата рождения')
        ws.write(0, 3, u'Возраст')


        # ws.write(0, 1, u'Пол')
        # ws.write(0, 2, u'Гражданство')
        # ws.write(0, 3, u'Дата рождения')
        # ws.write(0, 4, u'Тип трудоустройства')
        # ws.write(0, 5, u'Дополнительный доход (грн.)')
        # ws.write(0, 6, u'Расходы на еду (грн.)')
        # ws.write(0, 7, u'Расходы на здоровье (грн.)')
        # ws.write(0, 8, u'Расходы на одежду (грн.)')
        # ws.write(0, 9, u'Расходы на комунальные платежи (грн.)')
        # ws.write(0, 10, u'Расходы на алименты (грн.)')
        # ws.write(0, 11, u'Расходы на выплату кредитов (ежемесячные платежи, грн.)')
        # ws.write(0, 12, u'Баллы по секции')
        #
        # ws.write(0, 13, u'Образование')
        # ws.write(0, 14, u'Семейное положение')
        # # ws.write(0, 15, u'Адрес прописки и регистрации совпадает')
        # ws.write(0, 16, u'Город регистрации')
        # ws.write(0, 17, u'Город проживания')
        # ws.write(0, 18, u'Баллы по секции')
        #
        # ws.write(0, 19, u'Опыт работы (года)')
        # ws.write(0, 20, u'Доход (грн.)')
        # ws.write(0, 21, u'Категория должности')
        # ws.write(0, 22, u'Налоги за квартал (грн.)')
        # ws.write(0, 23, u'Количество сотрудников в организации')
        # ws.write(0, 24, u'Баллы по секции')
        #
        # ws.write(0, 25, u'Наличие квартиры')
        # ws.write(0, 26, u'Площадь квартиры, м2')
        # ws.write(0, 27, u'Состояние квартиры')
        # ws.write(0, 28, u'Наличие дома')
        # ws.write(0, 29, u'Площадь дома, м2')
        # ws.write(0, 30, u'Состояние дома')
        # ws.write(0, 31, u'Наличие квартиры')
        # ws.write(0, 32, u'Дата выпуска (год)')
        # ws.write(0, 33, u'Пробег (км)')
        # ws.write(0, 34, u'Состояние машины')
        # ws.write(0, 35, u'Наличие депозита')
        # ws.write(0, 36, u'Дата окончания вклада')
        # ws.write(0, 37, u'Размер депозита (грн.)')
        # ws.write(0, 38, u'Ежемесячные проценты (грн.)')
        # ws.write(0, 39, u'Наличие другой собственности')
        # ws.write(0, 40, u'Стоимость другой собственности (грн.)')
        # ws.write(0, 41, u'Баллы по секции')
        #
        # ws.write(0, 42, u'Люди, проживаущие за счет пользователя')
        # ws.write(0, 43, u'Люди, проживаущие с пользователем')
        # ws.write(0, 44, u'Наличие непогашеных кредитов')
        # ws.write(0, 45, u'Тип кредита')
        # ws.write(0, 46, u'Валюта кредита')
        # ws.write(0, 47, u'Дата окончания кредитного договора')
        # ws.write(0, 48, u'Первоначальная сумма кредита/займа')
        # ws.write(0, 49, u'Остаток по кредиту/займу')
        # ws.write(0, 50, u'Баллы по секции')
        # ws.write(0, 51, u'Итого баллов')
        #
        # for number, user in enumerate(users, start=1):
        #     if user.username != 'admin' and user.username != 'simzirok':
        #         profile = user.get_profile()
        #         education = profile.personal_information.get_education() if \
        #             profile.personal_information.get_education() else _(u'-')
        #         marital_status = profile.personal_information.get_marital_status() if \
        #             profile.personal_information.get_marital_status() else _(u'-')
        #         cohabitants = profile.personal_information.cohabitants if \
        #             profile.personal_information.cohabitants else _(u'-')
        #         dependents = profile.personal_information.get_dependents() if \
        #             profile.personal_information.get_dependents() else _(u'-')
        #
        #         address_equals = _(u'Совпадают') if \
        #             profile.address.equals else _(u'Не совпадают')
        #         address_city_real = profile.address.real.city if profile.address.real.city else _(u'-')
        #         address_city_official = profile.address.official.city if profile.address.official.city else _(u'-')
        #
        #         employment_type = profile.placement_information.normal_type() if \
        #             profile.placement_information.normal_type() else _(u'-')
        #         organisation_count_employees = profile.placement_information.get_employees_count() if \
        #             profile.placement_information.get_employees_count() else _(u'-')
        #         employment_category_position = profile.placement_information.get_category() if \
        #             profile.placement_information.get_category() else _(u'-')
        #         employment_income = profile.placement_information.income if \
        #             profile.placement_information.income else _(u'-')
        #         employment_term = profile.placement_information.term if \
        #             profile.placement_information.term else _(u'-')
        #         employment_tax_quarter = profile.placement_information.tax_quarter if \
        #             profile.placement_information.tax_quarter else _(u'-')
        #         employment_additional_income = profile.placement_information.additional_income.amount if \
        #             profile.placement_information.additional_income.amount else _(u'-')
        #
        #         charges_food = profile.placement_information.charges.food if \
        #             profile.placement_information.charges.food else _(u'-')
        #         charges_health = profile.placement_information.charges.health if \
        #             profile.placement_information.charges.health else _(u'-')
        #         charges_clothes = profile.placement_information.charges.clothes if \
        #             profile.placement_information.charges.clothes else _(u'-')
        #         charges_utilities = profile.placement_information.charges.utilities if \
        #             profile.placement_information.charges.utilities else _(u'-')
        #         charges_alimony = profile.placement_information.charges.alimony if \
        #             profile.placement_information.charges.alimony else _(u'-')
        #         charges_outstanding_loans = _(u'Есть') if \
        #             profile.placement_information.charges.outstanding_loans else _(u'Нет')
        #         charges_purpose_type = profile.placement_information.charges.get_purpose_type() if \
        #             profile.placement_information.charges.get_purpose_type() else _(u'-')
        #         charges_currency_credit = profile.placement_information.charges.currency_credit if \
        #             profile.placement_information.charges.currency_credit else _(u'-')
        #         charges_maturity_date = profile.placement_information.charges.maturity_date.strftime("%d-%m-%Y") if \
        #             profile.placement_information.charges.maturity_date else _(u'-')
        #         charges_initial_amount = profile.placement_information.charges.initial_amount if \
        #             profile.placement_information.charges.initial_amount else _(u'-')
        #         charges_current_amount = profile.placement_information.charges.current_amount if \
        #             profile.placement_information.charges.current_amount else _(u'-')
        #         charges_monthly_payment = profile.placement_information.charges.monthly_payment if \
        #             profile.placement_information.charges.monthly_payment else _(u'-')
        #
        #         assets_flat = profile.assets.is_flat() if profile.assets.is_flat() else _(u'-')
        #         assets_flat_area = profile.assets.flat_area if profile.assets.flat_area else _(u'-')
        #         assets_flat_state = profile.assets.get_flat_state() if profile.assets.get_flat_state() else _(u'-')
        #         assets_house = profile.assets.is_house() if profile.assets.is_house() else _(u'-')
        #         assets_house_area = profile.assets.house_area if profile.assets.house_area else _(u'-')
        #         assets_house_state = profile.assets.get_house_state() if profile.assets.get_house_state() else _(u'-')
        #         assets_car = profile.assets.is_car() if profile.assets.is_car() else _(u'-')
        #         assets_car_state = profile.assets.get_car_state() if profile.assets.get_car_state() else _(u'-')
        #         assets_car_year_manufacture = profile.assets.car_year_manufacture if \
        #             profile.assets.car_year_manufacture else _(u'-')
        #         assets_car_mileage = profile.assets.car_mileage if profile.assets.car_mileage else _(u'-')
        #         assets_deposits = profile.assets.is_deposits() if profile.assets.is_deposits() else _(u'-')
        #         assets_deposits_date_ends = profile.assets.deposits_maturity_date.strftime("%d-%m-%Y") if \
        #             profile.assets.deposits_maturity_date else _(u'-')
        #         assets_deposits_amount = profile.assets.deposits_amount \
        #             if profile.assets.deposits_amount else _(u'-')
        #         assets_monthly_percents = profile.assets.deposits_monthly_percents \
        #             if profile.assets.deposits_monthly_percents else _(u'-')
        #         assets_other = profile.assets.is_other_assets() \
        #             if profile.assets.is_other_assets() else _(u'-')
        #         assets_other_price = profile.assets.other_assets_price \
        #             if profile.assets.other_assets_price else _(u'-')
        #
        #         rating = self.scoring_service.calculate_for_user_section_points(profile.id)
        #
        #         ws.write(number, 0, number)
        #         ws.write(number, 1, u'%s' % profile.get_gender())
        #         ws.write(number, 2, u'%s' % profile.citizenship.title if profile.citizenship else '')
        #         ws.write(number, 3, u'%s' % profile.birthday.strftime("%d-%m-%Y"))
        #         ws.write(number, 4, u'%s' % employment_type)
        #         ws.write(number, 5, employment_additional_income)
        #         ws.write(number, 6, charges_food)
        #         ws.write(number, 7, charges_health)
        #         ws.write(number, 8, charges_clothes)
        #         ws.write(number, 9, charges_utilities)
        #         ws.write(number, 10, charges_alimony)
        #         ws.write(number, 11, charges_monthly_payment)
        #         ws.write(number, 12, u'%s' % rating['KI']['value'])
        #
        #         ws.write(number, 13, u'%s' % education)
        #         ws.write(number, 14, u'%s' % marital_status)
        #         # ws.write(number, 15, u'%s' % address_equals)
        #         ws.write(number, 16, u'%s' % address_city_real)
        #         ws.write(number, 17, u'%s' % address_city_official)
        #         ws.write(number, 18, u'%s' % rating['PD']['value'])
        #
        #         ws.write(number, 19, u'%s' % employment_term)
        #         ws.write(number, 20, employment_income)
        #         ws.write(number, 21, u'%s' % employment_category_position)
        #         ws.write(number, 22, u'%s' % employment_tax_quarter)
        #         ws.write(number, 23, u'%s' % organisation_count_employees)
        #         ws.write(number, 24, rating['E']['value'])
        #
        #         ws.write(number, 25, u'%s' % assets_flat)
        #         ws.write(number, 26, u'%s' % assets_flat_area)
        #         ws.write(number, 27, u'%s' % assets_flat_state)
        #         ws.write(number, 28, u'%s' % assets_house)
        #         ws.write(number, 29, u'%s' % assets_house_area)
        #         ws.write(number, 30, u'%s' % assets_house_state)
        #         ws.write(number, 31, u'%s' % assets_car)
        #         ws.write(number, 32, u'%s' % assets_car_year_manufacture)
        #         ws.write(number, 33, u'%s' % assets_car_mileage)
        #         ws.write(number, 34, u'%s' % assets_car_state)
        #         ws.write(number, 35, u'%s' % assets_deposits)
        #         ws.write(number, 36, u'%s' % assets_deposits_date_ends)
        #         ws.write(number, 37, u'%s' % assets_deposits_amount)
        #         ws.write(number, 38, u'%s' % assets_monthly_percents)
        #         ws.write(number, 39, u'%s' % assets_other)
        #         ws.write(number, 40, u'%s' % assets_other_price)
        #         ws.write(number, 41, u'%s' % rating['A']['value'])
        #
        #         ws.write(number, 42, u'%s' % dependents)
        #         ws.write(number, 43, u'%s' % cohabitants)
        #         ws.write(number, 44, charges_outstanding_loans)
        #         ws.write(number, 45, u'%s' % charges_purpose_type)
        #         ws.write(number, 46, u'%s' % charges_currency_credit)
        #         ws.write(number, 47, charges_maturity_date)
        #         ws.write(number, 48, charges_initial_amount)
        #         ws.write(number, 49, charges_current_amount)
        #         ws.write(number, 50, u'%s' % rating['L']['value'])
        #
        #         total_score = rating['KI']['value'] + rating['PD']['value'] + rating['E']['value'] + \
        #                       rating['A']['value'] + rating['L']['value']
        #         ws.write(number, 51, u'%s' % total_score)

        print u'Сохраняем отчет'
        file_name = '/report_borrowers_%s.xls' % date.today()
        path_to_file = self.path_to_report + file_name
        wb.save(path_to_file)

        print u'Отправляем письма с отчетом'
        ## send email to managers
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