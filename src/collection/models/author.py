from collection.models.common import CollectionModel, TranslatableModel
from collection.models.language import Language
from django.db import models


class AuthorQuerySet(models.QuerySet):
    def invidivuals(self):
        return self.filter(members_count=0)

    def groups(self):
        return self.filter(members_count__gte=1)


class AuthorManager(models.Manager.from_queryset(AuthorQuerySet)):
    GROUP_NO_MEMBERS = models.Q(name='__group_no_members__')

    def get_queryset(self):
        return super(AuthorManager, self).get_queryset() \
            .annotate(members_count=models.Count('members')) \
            .filter(~self.GROUP_NO_MEMBERS)

    def individuals(self):
        return self.get_queryset().invidivuals()

    def groups(self):
        return self.get_queryset().groups()


class Author(CollectionModel, TranslatableModel):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    members = models.ManyToManyField(
        'self',
        symmetrical=False
    )

    # Custom manager to ignore the special __group_no_members__ entity
    objects = AuthorManager()

    # Default manager still accessible through _objects
    _objects = models.Manager()

    def is_group(self):
        return self.members.count() > 0

    def set_group(self, group=True):
        if group:
            def_member = Author._objects.get(AuthorManager.GROUP_NO_MEMBERS)
            self.members.add(def_member)
        else:
            self.members.all().delete()

    def get_members(self):
        return self.members.all()
