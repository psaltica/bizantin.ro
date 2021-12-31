from django.db import models
from enum import Flag


class Person(models.Model):
    name = models.CharField(max_length=200)


class MusicalText(models.Model):

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
    author = models.ForeignKey(Person)

    original = models.ForeignKey(
        'self',
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

    mode = models.IntegerField()

    notes = models.CharField(max_length=512)
