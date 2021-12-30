from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)


class MusicalText(models.Model):

    CONTRIBUTION_TYPES = [
        ('C', "Composed"),
        ('T', "Translated"),
        ('P', "Processed"),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Person)

    original = models.ForeignKey(
        'self',
        blank=True
    )

    contribution = models.CharField(
        max_length=1,
        choices=CONTRIBUTION_TYPES,
        default='C'
    )

    notes = models.CharField(max_length=512)
