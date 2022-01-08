from collection.models.common import TranslatableModel
from django.contrib.contenttypes.fields import GenericRelation
from django.core.cache import cache
from django.db import models

class Language(TranslatableModel):
    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    code = models.CharField(
        max_length=2,
        primary_key=True,
        editable=False
    )

    name = models.CharField(
        max_length=32,
        unique=True
    )

    # Override 'lang' because it is replaced by 'code' here
    lang = None

    def get_default():
        default = cache.get('lang_default')
        if (default is None):
            default = Language.objects.get(code='ro')
            cache.set('lang_default', default)

        return default
