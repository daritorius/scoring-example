# -*- coding: utf-8 -*-
from core.main.base.BaseModel import BaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LocalScoring(BaseModel):
    age_score = models.ForeignKey('LocalAgeScore', blank=True, null=True)
    placement_score = models.ForeignKey('LocalPlacementScoring', blank=True, null=True)
    personal_score = models.ForeignKey('LocalPersonalScoring', blank=True, null=True)
    assets_score = models.ForeignKey('LocalAssetsScoring', blank=True, null=True)
    loan_score = models.ForeignKey('LocalLoanScoring', blank=True, null=True)
    total_score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalScoringService import LocalScoringService
        service = LocalScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_scoring'
        verbose_name = _(u'Local scoring')
        verbose_name_plural = _(u'Local scoring')


class LocalAgeScore(BaseModel):
    score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalAgeScoreService import LocalAgeScoreService
        service = LocalAgeScoreService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_age_scoring'
        verbose_name = _(u'Local age scoring')
        verbose_name_plural = _(u'Local age scoring')


class LocalPlacementScoring(BaseModel):
    placement_type_score = models.IntegerField(default=0, max_length=255)
    placement_income_score = models.IntegerField(default=0, max_length=255)
    placement_clean_income = models.IntegerField(default=0, max_length=255)
    work_score = models.IntegerField(default=0, max_length=255)
    term_score = models.IntegerField(default=0, max_length=255)
    wage_score = models.IntegerField(default=0, max_length=255)
    category_position_score = models.IntegerField(default=0, max_length=255)
    tax_score = models.IntegerField(default=0, max_length=255)
    count_employees_score = models.IntegerField(default=0, max_length=255)
    total_score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalPlacementScoringService import LocalPlacementScoringService
        service = LocalPlacementScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_placement_scoring'
        verbose_name = _(u'Local placement scoring')
        verbose_name_plural = _(u'Local placement scoring')


class LocalPersonalScoring(BaseModel):
    education_score = models.IntegerField(default=0, max_length=255)
    marital_status_score = models.IntegerField(default=0, max_length=255)
    official_address_score = models.IntegerField(default=0, max_length=255)
    real_address_score = models.IntegerField(default=0, max_length=255)
    identity_addresses_score = models.IntegerField(default=0, max_length=255)
    total_score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalPersonalScoringService import LocalPersonalScoringService
        service = LocalPersonalScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_personal_scoring'
        verbose_name = _(u'Local personal scoring')
        verbose_name_plural = _(u'Local personal scoring')


class LocalAssetsScoring(BaseModel):
    available_assets_score = models.IntegerField(default=0, max_length=255)
    flat_score = models.IntegerField(default=0, max_length=255)
    flat_area_score = models.IntegerField(default=0, max_length=255)
    flat_status_score = models.IntegerField(default=0, max_length=255)
    house_score = models.IntegerField(default=0, max_length=255)
    house_area_score = models.IntegerField(default=0, max_length=255)
    house_status_score = models.IntegerField(default=0, max_length=255)
    car_score = models.IntegerField(default=0, max_length=255)
    car_status_score = models.IntegerField(default=0, max_length=255)
    car_lifetime_score = models.IntegerField(default=0, max_length=255)
    car_mileage_car_score = models.IntegerField(default=0, max_length=255)
    deposit_score = models.IntegerField(default=0, max_length=255)
    deposit_amount_score = models.IntegerField(default=0, max_length=255)
    deposit_percents_score = models.IntegerField(default=0, max_length=255)
    deposit_maturity_date_score = models.IntegerField(default=0, max_length=255)
    other_assets_score = models.IntegerField(default=0, max_length=255)
    total_score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalAssetsScoringService import LocalAssetsScoringService
        service = LocalAssetsScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_assets_scoring'
        verbose_name = _(u'Local assets scoring')
        verbose_name_plural = _(u'Local assets scoring')


class LocalLoanScoring(BaseModel):
    outstanding_loan_score = models.IntegerField(default=0, max_length=255)
    amount_loan_score = models.IntegerField(default=0, max_length=255)
    repayment_percent_score = models.IntegerField(default=0, max_length=255)
    days_to_repayment_score = models.IntegerField(default=0, max_length=255)
    monthly_payment_score = models.IntegerField(default=0, max_length=255)
    debt_burden_score = models.IntegerField(default=0, max_length=255)
    dependents_score = models.IntegerField(default=0, max_length=255)
    total_score = models.IntegerField(default=0, max_length=255)

    def __unicode__(self):
        return u'%s' % self.id

    def save(self, *args, **kwargs):
        from core.scoring.apps.local.services.LocalLoanScoringService import LocalLoanScoringService
        service = LocalLoanScoringService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_loan_scoring'
        verbose_name = _(u'Local loan scoring')
        verbose_name_plural = _(u'Local loan scoring')