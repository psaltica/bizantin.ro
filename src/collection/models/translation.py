from collection.models.common import CollectionModel, TranslatableModel
from collection.models.language import Language
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from functools import reduce


class Translation(CollectionModel):
    def _get_translatable_model_choices():
        translatable_models = TranslatableModel.__subclasses__()
        expressions = [
            models.Q(app_label='collection', model=cls.__name__.lower())
            for cls in translatable_models
        ]

        return reduce(lambda a, b: a | b, expressions)

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
        limit_choices_to=_get_translatable_model_choices(),
    )

    field = models.CharField(max_length=32)

    def clean(self):
        if self.original.lang == self.lang:
            raise ValidationError('Cannot translate to the same lang as the original.')

    class Meta:
        unique_together = ['lang', 'original_id', 'field']
