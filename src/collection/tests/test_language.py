from collection.models.language import Language
from django.test import TestCase


class LanguageDefaultTestCase(TestCase):
    databases = ['content']

    def test_initial_languages(self):
        lang_query = Language.objects.all()

        languages = {}
        for lang in lang_query:
            languages[lang.code] = lang.name

        self.assertTrue('en' in languages)
        self.assertTrue('ro' in languages)
        self.assertTrue('el' in languages)
        self.assertTrue('ar' in languages)

    def test_default_language(self):
        default_lang = Language.get_default()
        self.assertEqual(default_lang.code, 'ro')
