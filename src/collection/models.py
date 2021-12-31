from django.db import models
from enum import Flag

import datetime
import uuid


class CollectionModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Person(CollectionModel):
    name = models.CharField(max_length=200)


class MusicalText(CollectionModel):

    CONTRIBUTION_TYPES = [
        ('C', "Composed"),
        ('T', "Translated"),
        ('P', "Processed"),
    ]

    LANGUAGES = [
        ("ar", "Arabic"),
        ("en", "English"),
        ("gr", "Greek"),
        ("ro", "Romanian"),
    ]

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
    author = models.ForeignKey(
        Person,
        on_delete=models.PROTECT
    )

    original = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True
    )

    lang = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default="ro"
    )

    contribution = models.CharField(
        max_length=1,
        choices=CONTRIBUTION_TYPES,
        default='C'
    )

    date = models.DateField(
        default=datetime.date.today
    )

    date_accuracy = models.PositiveSmallIntegerField(
        choices=DateAccuracy.choices,
        default=DateAccuracy.YEAR
    )

    mode = models.PositiveSmallIntegerField()

    notes = models.CharField(max_length=512)
