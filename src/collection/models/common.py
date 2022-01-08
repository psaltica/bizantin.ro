from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

import uuid


class CollectionModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class TranslatableModel(models.Model):
    lang = models.ForeignKey(
        'Language',
        on_delete=models.PROTECT
    )

    translations = GenericRelation(
        'Translation',
        content_type_field='original_type',
        object_id_field='original_id'
    )

    def get_translations_for(self, field):
        translations = {}
        query = self.translations.filter(field=field)

        for t in query:
            translations[t.lang.code] = t.text

        return translations

    class Meta:
        abstract = True
