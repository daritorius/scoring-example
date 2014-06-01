# -*- coding: utf-8 -*-
from core.emails.models import EmailTemplate
from core.main.base.services.BaseService import BaseService
from django.utils.translation import ugettext as _


class EmailTemplateService(BaseService):
    model_instance = EmailTemplate

    def get_email_template_by_title(self, title):
        try:
            return self.get_item(title=title)
        except EmailTemplate.DoesNotExist:
            return None

    def get_restore_password_template(self):
        return self.get_email_template_by_title('restore_password')