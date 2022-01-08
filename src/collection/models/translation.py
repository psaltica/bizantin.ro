from collection.models.common import CollectionModel
from collection.models.language import Language
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Translation(CollectionModel):
    lang = models.ForeignKey(
        Language,
        on_delete=models.PROTECT
    )

    text = models.CharField(max_length=512)

    original = GenericForeignKey('original_type', 'original_id')
    original_id = models.UUIDField()
    original_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    field = models.CharField(max_length=32)
