from django.contrib.auth.models import User
from django.test import Client, TestCase
from article import models


class TestCaseWithUser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username='jetbird')
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()


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


class HomeViewTest(TestCaseWithUser):

    def test_home_view_returns_response(self):

        response = self.client.get('/')

        self.assertIn('<h1>HackerScoops</h1>', response.content)

    def test_view_context_contains_last_ten_articles(self):
        for ii in range(15):
            models.Article.objects.create(
                title='Art %s' % (ii,),
                author=self.user,
                body=''
            )

        response = self.client.get('/')

        self.assertEqual(len(response.context['articles']), 10)
        self.assertEqual(response.context['articles'][0].title, 'Art 0')
        self.assertEqual(response.context['articles'][9].title, 'Art 9')


class  ArticleViewTest(TestCaseWithUser):

    def test_view_article_displays_the_article(self):
        models.Article.objects.create(
            title='My Title', author=self.user, body='', slug='article-name'
        )

        response = self.client.get('/article/article-name')

        self.assertEqual(response.context['article'].title, 'My Title')
