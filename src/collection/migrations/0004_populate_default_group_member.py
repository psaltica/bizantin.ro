# Generated by Django 4.0 on 2022-01-08 21:04

from django.db import migrations


def populate_default_group_member(apps, schema_editor):
    Language = apps.get_model('collection', 'Language')
    Author = apps.get_model('collection', 'Author')

    default_lang = Language.objects.get(code='en')
    default_group_member = Author(
        name='__group_no_members__',
        lang=default_lang
    )

    db_alias = schema_editor.connection.alias
    Author.objects.using(db_alias).bulk_create([default_group_member])


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_populate_initial_language_codes'),
    ]

    operations = [
        migrations.RunPython(populate_default_group_member)
    ]