# -*- coding: utf-8 -*-
import datetime
import logging
import hashlib
from core.emails.models import Email
from core.emails.plain_models import EmailPlainModel
from core.emails.services.BaseUtils import BaseUtils
from core.main.base.services.BaseService import BaseService
from core.emails.services.EmailTemplateService import EmailTemplateService
from core.main.site.services.SiteService import SiteService
from core.users.profiles.services.UserProfileService import UserProfileService
from django.utils.translation import ugettext as _

logger = logging.getLogger()


class EmailService(BaseService):
    model_instance = Email
    logger = logging.getLogger('emails')
    site_service = SiteService()
    email_template_service = EmailTemplateService()
    profile_service = UserProfileService()

    def save_email(self, email_to, email_data, template):
        if template:
            email_data['site'] = self.site_service.get_current().domain
            html_content = BaseUtils.parse_template(template.body, email_data)
            subject_content = BaseUtils.parse_template(template.subject, email_data)
            email_data = EmailPlainModel(subject=subject_content, body=html_content, email_to=email_to)
            email = self.create(email_data)
            self.logger.info(u'Email created [subject: %s| body: %s| email_to: %s]' % (
                email.subject, email.body, email.email_to))
            return email

    def get_all_not_sent_emails(self):
        return self.select(status=Email.STATUS_UNDEFINED)