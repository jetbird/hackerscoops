from django.test import Client, TestCase
from article import models

class CategoryTest(TestCase):

    def test_model_can_be_created(self):

        category = models.Category.objects.create(
            name='Cat 1', description='Category 1 is long')

        self.assertEqual(category.name, 'Cat 1')
        self.assertEqual(category.description, 'Category 1 is long')

    def test_unicode_representation(self):
        category = models.Category.objects.create(
            name='Cat 2', description='Category 2 is long')

        self.assertEqual(unicode(category), 'Cat 2')


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view_returns_response(self):

        response = self.client.get('/')

        self.assertIn('<h1>HackerScoops</h1>', response.content)
