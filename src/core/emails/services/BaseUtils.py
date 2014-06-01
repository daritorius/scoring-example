# coding=utf-8
from core.users.profiles.services.UserProfileService import UserProfileService
from django.template import Template, Context


class BaseUtils(object):
    profile_service = UserProfileService()

    @classmethod
    def parse_template(cls, template, data):
        assert isinstance(data, dict)
        return Template(template).render(Context(data))