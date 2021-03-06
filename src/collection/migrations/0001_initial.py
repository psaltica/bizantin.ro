# Generated by Django 4.0 on 2022-01-02 17:24

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(blank=True, to='collection.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MusicalText',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_secular', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('lang', models.CharField(choices=[('ar', 'Arabic'), ('en', 'English'), ('gr', 'Greek'), ('ro', 'Romanian')], default='ro', max_length=2)),
                ('contribution', models.CharField(choices=[('C', 'Composed'), ('T', 'Translated'), ('P', 'Processed')], default='C', max_length=1)),
                ('date', models.DateField(default=datetime.date.today)),
                ('date_accuracy', models.PositiveSmallIntegerField(choices=[(0, 'Day'), (1, 'Month'), (2, 'Year'), (3, 'Decade'), (4, 'Century')], default=2)),
                ('mode', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(1)])),
                ('notes', models.CharField(max_length=512)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.author')),
                ('original', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='collection.musicaltext')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lang', models.CharField(choices=[('ar', 'Arabic'), ('en', 'English'), ('gr', 'Greek'), ('ro', 'Romanian')], default='ro', max_length=2)),
                ('text', models.CharField(max_length=512)),
                ('original_id', models.UUIDField()),
                ('original_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('date', models.DateField(default=datetime.date.today)),
                ('date_accuracy', models.PositiveSmallIntegerField(choices=[(0, 'Day'), (1, 'Month'), (2, 'Year'), (3, 'Decade'), (4, 'Century')], default=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.author')),
                ('musical_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.musicaltext')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('online_access', models.URLField()),
                ('musical_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.musicaltext')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
