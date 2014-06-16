# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCardModel import BaseScoringCardModel
from django.utils.translation import ugettext as _


class LocalAgeScoringCard(BaseScoringCardModel):
    def save(self, *args, **kwargs):
        from core.scoring.apps.local.scoring_cards.age_cards.services.AgeScoringCardService import AgeScoringCardService
        service = AgeScoringCardService()
        service.cache_service.delete_pattern(u'%s*' % service.__class__.__name__)
        return super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        db_table = 'local_age_scoring_card'
        verbose_name = _(u'Local age scoring card')
        verbose_name_plural = _(u'Local age scoring cards')