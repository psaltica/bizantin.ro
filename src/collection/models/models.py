from collection.models.common import CollectionModel, TranslatableModel
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from enum import Flag

from collection.models.author import Author

import datetime
import uuid


class DateAccuracy(models.IntegerChoices):
    DAY     = 0
    MONTH   = 1
    YEAR    = 2
    DECADE  = 3
    CENTURY = 4


class MusicalText(CollectionModel, TranslatableModel):

    class ContributionTypes(models.TextChoices):
        COMPOSED   = 'C', "Composed"
        TRANSLATED = 'T', "Translated"
        PROCESSED  = 'P', "Processed"

    class Modes(Flag):
        A    = 0b00000001
        B    = 0b00000010
        C    = 0b00000100
        D    = 0b00001000
        PL_A = 0b00010000
        PL_B = 0b00100000
        PL_C = 0b01000000
        PL_D = 0b10000000

    is_secular = models.BooleanField(default=False)

    title = models.CharField(max_length=200)
    translations = GenericRelation(
        'Translation',
        content_type_field='original_type',
        object_id_field='original_id'
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    original = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    contribution = models.CharField(
        max_length=1,
        choices=ContributionTypes.choices,
        default=ContributionTypes.COMPOSED
    )

    date = models.DateField(default=datetime.date.today)
    date_accuracy = models.PositiveSmallIntegerField(
        choices=DateAccuracy.choices,
        default=DateAccuracy.YEAR
    )

    mode = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(0b11111111),
            MinValueValidator(0b00000001),
        ]
    )

    notes = models.CharField(max_length=512)


class Performance(CollectionModel):
    musical_text = models.ForeignKey(
        MusicalText,
        on_delete=models.CASCADE
    )

    performer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    online_access = models.URLField()


class Publication(CollectionModel, TranslatableModel):
    musical_text = models.ForeignKey(
        MusicalText,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    translations = GenericRelation(
        'Translation',
        content_type_field='original_type',
        object_id_field='original_id'
    )

    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)

    date = models.DateField(default=datetime.date.today)
    date_accuracy = models.PositiveSmallIntegerField(
        choices=DateAccuracy.choices,
        default=DateAccuracy.YEAR
    )
