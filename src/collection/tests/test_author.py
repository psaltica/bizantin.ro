from collection.models.author import Author
from collection.models.language import Language
from django.test import TestCase


class AuthorDefaultTestCase(TestCase):
    databases = ['content']

    def test_default_group_member(self):
        default_member = Author._objects.get(name='__group_no_members__')
        self.assertEqual(default_member.is_group(), False)

    def test_author_manager(self):
        self.assertEqual(Author._objects.count(), 1)
        self.assertEqual(Author.objects.count(), 0)


class AuthorCreateTestCase(TestCase):
    databases = ['content']

    def setUp(self):
        default_lang = Language.get_default()

        individual = Author.objects.create(name='individual', lang=default_lang)
        group = Author.objects.create(name='group', lang=default_lang)
        group.set_group(True)

        individual.save()
        group.save()

    def test_group_and_individual(self):
        self.assertEqual(Author.objects.groups().count(), 1)
        self.assertEqual(Author.objects.individuals().count(), 1)

        individual = Author.objects.individuals()[0]
        group = Author.objects.groups()[0]

        self.assertEqual(individual.name, 'individual')
        self.assertEqual(group.name, 'group')
