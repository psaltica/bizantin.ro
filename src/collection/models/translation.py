from collection.models.common import CollectionModel, TranslatableModel
from collection.models.language import Language
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models

from functools import reduce


class Translation(CollectionModel):
    TRANSLATABLE_MODELS = reduce(lambda a, b: a | b, [
        models.Q(
            app_label='collection',
            model=cls.__name__.lower()
        ) for cls in TranslatableModel.__subclasses__()
    ])

    lang = models.ForeignKey(
        Language,
        on_delete=models.PROTECT
    )

    text = models.CharField(max_length=512)

    original = GenericForeignKey('original_type', 'original_id')
    original_id = models.UUIDField()
    original_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=TRANSLATABLE_MODELS
    )

    field = models.CharField(max_length=32)

    def clean(self):
        if not self.original.__class__ in TranslatableModel.__subclasses__():
            raise ValidationError('Translation refers to non-translatable original')

        if self.original.lang == self.lang:
            raise ValidationError('Cannot translate to the same lang as the original.')

    class Meta:
        unique_together = ['lang', 'original_id', 'field']
