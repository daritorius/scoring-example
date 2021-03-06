# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.db import models
from django.utils.translation import ugettext as _


class BaseLocalPersonalMaritalStatusCard(BaseModel):
    FALSE_MARITAL_STATUS = 0
    TRUE_MARITAL_STATUS = 1
    WIDOW_MARITAL_STATUS = 2
    DIVORCED_MARITAL_STATUS = 3

    MARITAL_STATUSES = (
        (FALSE_MARITAL_STATUS, u'Незамужем/Неженат'),
        (TRUE_MARITAL_STATUS, u'Замужем/Женат'),
        (WIDOW_MARITAL_STATUS, u'Вдова/Вдовец'),
        (DIVORCED_MARITAL_STATUS, u'Разведена/Разведен'),
    )

    key = models.IntegerField(_(u'Значение'), default=FALSE_MARITAL_STATUS, choices=MARITAL_STATUSES, max_length=255,
                              blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    class Meta:
        abstract = True
        ordering = ['value']


class LocalPersonalEducationCard(BaseModel):
    HIGH_EDUCATION = 0
    MIDDLE_EDUCATION = 1
    MIDDLE_TECH_EDUCATION = 2
    NOT_FINISHED_HIGH_EDUCATION = 3
    TWO_OR_MORE_HIGH_EDUCATION = 4
    DEGREE_EDUCATION = 4
    NOT_FINISHED_MIDDLE_EDUCATION = 5

    EDUCATION_TYPES = (
        (HIGH_EDUCATION, u'Высшее'),
        (MIDDLE_EDUCATION, u'Среднее'),
        (MIDDLE_TECH_EDUCATION, u'Серднее техническое'),
        (NOT_FINISHED_HIGH_EDUCATION, u'Неоконченное высшее'),
        (TWO_OR_MORE_HIGH_EDUCATION, u'2 и более высших образования'),
        (DEGREE_EDUCATION, u'Ученая степень'),
        (NOT_FINISHED_MIDDLE_EDUCATION, u'Неоконченное среднее образование'),
    )

    key = models.IntegerField(_(u'Значение'), default=NOT_FINISHED_MIDDLE_EDUCATION, choices=EDUCATION_TYPES,
                              max_length=255, blank=True, null=True)
    value = models.IntegerField(_(u'Баллы'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.value)

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalPersonalEducationCardService import \
            LocalPersonalEducationCardService

        service = LocalPersonalEducationCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_personal_education_card'
        verbose_name = _(u'Local personal education')
        verbose_name_plural = _(u'Local personal education')
        ordering = ['value']


class LocalPersonalMaritalStatusNormalCard(BaseLocalPersonalMaritalStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalMaritalStatusNormalCardService import \
            LocalMaritalStatusNormalCardService

        service = LocalMaritalStatusNormalCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_personal_marital_normal_card'
        verbose_name = _(u'Local personal marital normal')
        verbose_name_plural = _(u'Local personal marital normal')


class LocalPersonalMaritalStatusBadCard(BaseLocalPersonalMaritalStatusCard):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalMaritalStatusBadCardService import \
            LocalMaritalStatusBadCardService

        service = LocalMaritalStatusBadCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_personal_marital_bad_card'
        verbose_name = _(u'Local personal marital bad')
        verbose_name_plural = _(u'Local personal marital bad')


class LocalPersonalIdentityAddressesCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalIdentityAddressesCardService import \
            LocalIdentityAddressesCardService

        service = LocalIdentityAddressesCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_personal_identity_addresses_card'
        verbose_name = _(u'Local personal identity addr')
        verbose_name_plural = _(u'Local personal identity addr')