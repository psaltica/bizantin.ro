from collection.models.common import CollectionModel, TranslatableModel
from django.db import models


class Category(CollectionModel, TranslatableModel):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )

    def is_base_category(self):
        return self.parent_id is None

    def get_base_category(self):
        c = self
        while not c.is_base_category():
            c = c.parent

        return c.name

    def is_leaf_category(self):
        return not Category.objects.filter(parent=self.id).exists()
