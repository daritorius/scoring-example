# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings
import djcelery
from datetime import timedelta
from django.conf import settings as s

djcelery.setup_loader()

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERYBEAT_SCHEDULE = {
    # 'process_repayments': {
    #     'task': 'core.finance_system.payments.tasks.process_repayments',
    #     'schedule': timedelta(minutes=5),
    #     'args': ()
    # },
    # 'update_currencies': {
    #     'task': 'core.currency.tasks.update_currencies',
    #     'schedule': settings.crontab(minute=0, hour='*/3'),
    #     'args': ()
    # },
    # 'report_projects': {
    #     'task': 'core.main.reports.tasks.process_project_report',
    #     'schedule': settings.crontab(day_of_week=5, hour=12, minute=0),
    #     'args': ()
    # },
    # 'report_big_daily': {
    #     'task': 'core.main.reports.tasks.process_big_daily_report',
    #     'schedule': settings.crontab(minute=0, hour=3),
    #     'args': ()
    # },
}

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERYD_MAX_TASKS_PER_CHILD = 1
CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True
CELERYD_PREFETCH_MULTIPLIER = 1
# CELERY_ACKS_LATE = True