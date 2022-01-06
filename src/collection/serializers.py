from rest_framework import serializers
from . import models


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Translation
        fields = ['lang', 'text']


class AuthorSerializer(serializers.ModelSerializer):
    name_translations = TranslationSerializer(many=True)

    class Meta:
        model = models.Author
        fields = ['id', 'name', 'name_translations']


class MusicalTextSerializer(serializers.ModelSerializer):
    title_translations = TranslationSerializer(many=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    original = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.MusicalText
        fields = [
            'id',
            'is_secular',
            'title',
            'title_translations',
            'author',
            'original',
            'lang',
            'contribution',
            'date',
            'date_accuracy',
            'mode',
            'notes',
        ]


class PerformanceSerializer(serializers.ModelSerializer):
    performer = serializers.PrimaryKeyRelatedField(read_only=True)
    musical_text = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Performance
        fields = ['id', 'performer', 'musical_text', 'online_access']


class PublicationSerializer(serializers.ModelSerializer):
    musical_text = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    title_translations = TranslationSerializer(many=True)

    class Meta:
        model = models.Publication
        fields = [
            'id',
            'musical_text',
            'author',
            'title',
            'title_translations',
            'publisher',
            'isbn',
            'date',
            'date_accuracy',
        ]
