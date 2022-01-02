from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from enum import Flag

import datetime
import uuid


class Constraints:
    AUTHOR_TYPES = [
        models.Q(app_label='collection', model='person'),
        models.Q(app_label='collection', model='group'),
    ]


class Languages(models.TextChoices):
    ARABIC   = "ar", "Arabic"
    ENGLISH  = "en", "English"
    GREEK    = "gr", "Greek"
    ROMANIAN = "ro", "Romanian"


class CollectionModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Author(CollectionModel):
    name = models.CharField(max_length=200)
    name_translations = GenericRelation(
        'Translation',
        content_type_field='original_type',
        object_id_field='original_id'
    )

    compositions = GenericRelation(
        'MusicalText',
        content_type_field='author_type',
        object_id_field='author_id'
    )

    performances = GenericRelation(
        'Performance',
        content_type_field='performer_type',
        object_id_field='performer_id'
    )

    class Meta:
        abstract = True


class Person(Author):
    pass


class Group(Author):
    members = models.ManyToManyField(Person)


class MusicalText(CollectionModel):

    class ContributionTypes(models.TextChoices):
        COMPOSED   = 'C', "Composed"
        TRANSLATED = 'T', "Translated"
        PROCESSED  = 'P', "Processed"

    class DateAccuracy(models.IntegerChoices):
        DAY     = 0
        MONTH   = 1
        YEAR    = 2
        DECADE  = 3
        CENTURY = 4

    class Modes(Flag):
        A    = 0b00000001
        B    = 0b00000010
        C    = 0b00000100
        D    = 0b00001000
        PL_A = 0b00010000
        PL_B = 0b00100000
        PL_C = 0b01000000
        PL_D = 0b10000000

    title = models.CharField(max_length=200)
    title_translations = GenericRelation(
        'Translation',
        content_type_field='original_type',
        object_id_field='original_id'
    )

    author = GenericForeignKey('author_type', 'author_id')
    author_id = models.UUIDField()
    author_type = models.ForeignKey(
        ContentType,
        limit_choices_to=Constraints.AUTHOR_TYPES,
        on_delete=models.CASCADE
    )

    original = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True
    )

    lang = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.ROMANIAN
    )

    contribution = models.CharField(
        max_length=1,
        choices=ContributionTypes.choices,
        default=ContributionTypes.COMPOSED
    )

    date = models.DateField(
        default=datetime.date.today
    )

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


class Translation(CollectionModel):
    lang = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.ROMANIAN
    )

    text = models.CharField(max_length=512)

    original = GenericForeignKey('original_type', 'original_id')
    original_id = models.UUIDField()
    original_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )


class Performance(CollectionModel):
    musical_text = models.ForeignKey(
        MusicalText,
        on_delete=models.CASCADE
    )

    performer = GenericForeignKey('performer_type', 'performer_id')
    performer_id = models.UUIDField()
    performer_type = models.ForeignKey(
        ContentType,
        limit_choices_to=Constraints.AUTHOR_TYPES,
        on_delete=models.CASCADE
    )

    online_access = models.URLField()
