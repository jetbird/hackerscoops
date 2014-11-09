from django.contrib.auth.models import User
from django.test import Client, TestCase
from article import models
from django.contrib.auth import authenticate, login
from article.views import normalize_query, get_query


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
        for ii in range(10):
            models.Article.objects.create(
                title='Art %s' % (ii,),
                author=self.user,
                body=''
            )

        response = self.client.get('/')

        self.assertEqual(len(response.context['articles']), 10)
        self.assertEqual(response.context['articles'][0].title, 'Art 9')
        self.assertEqual(response.context['articles'][9].title, 'Art 0')


class  ArticleViewTest(TestCaseWithUser):

    def test_view_article_displays_the_article(self):
        models.Article.objects.create(
            title='My Title', author=self.user, body='', slug='article-name'
        )

        response = self.client.get('/article/article-name')

        self.assertEqual(response.context['article'].title, 'My Title')


class CategoryViewTest(TestCaseWithUser):

    def test_category_displays_the_articles(self):

        my_article = models.Article(title='Title', author=self.user, body='',
             slug='article-name')
        my_article.save()
        test_category = models.Category(name='TestCategory')
        test_category.save()
        my_article.categories.add(test_category)


        response = self.client.get('/category/TestCategory')

        self.assertEqual(response.context['article_list'][0].title,
            models.Article.objects.filter
            (categories__name__startswith='TestCategory')[0].title)


class CommentTest(TestCaseWithUser):

    def test_if_user_can_comment(self):


        test_user=User.objects.create(username='j13',password='j13')
        response = self.client.post('/accounts/login/',{'username':'j13',
        'password':'j13'}
                )
        second_response = self.client.post('/article/holy_bitcoin',
                {'author':test_user,'content':'test'})
        self.assertEqual(response.status_code,200)
        self.assertEqual(second_response.status_code,200)


class AboutViewTest(TestCaseWithUser):

    def test_if_about_returns_200(self):
        response = self.client.get('/about/Us')
        self.assertEqual(response.status_code,200)


class QueryStringTest(TestCaseWithUser):

    def test_query_can_normalized(self):
        self.assertEqual(normalize_query('jetbird loves python'),
                ['jetbird', 'loves', 'python'])

    def test_get_query_works(self):

        my_article = models.Article.objects.create(
                title='Title', author=self.user, body='', slug='article-name'
                )
        query = get_query('Title', ['title', 'body'])
        searchresult = models.Article.objects.filter(query)
        self.assertEqual(searchresult[0], my_article)
