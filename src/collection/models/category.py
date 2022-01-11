from collection.models.common import CollectionModel, TranslatableModel
from django.db import models


class Category(CollectionModel, TranslatableModel):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    parent = models.ForeignKey(
        'Self',
        on_delete=models.CASCADE
    )
