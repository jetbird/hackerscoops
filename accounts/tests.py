from django.test import TestCase, Client
from accounts.forms import UserForm, UserProfileForm

# Create your tests here.


class TestForms(TestCase):
    def test_userform_data_is_valid(self):
        form = UserForm(data={'username':'j13',
            'email':'j13@gmail.com', 'password':'o13$#'})
        self.assertEqual(form.is_valid(), True)

    def test_userprofileform_is_valid(self):
        form = UserProfileForm(data={'website':'myweb13.com'})
        self.assertEqual(form.is_valid(), True)


class RegisterViewTest(TestCase):
    def setUP(self):
        self.client = Client()

    def test_register_view_returns_200(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register Here')
        self.assertContains(response, 'Accounts App')

    def test_if_user_can_register(self):
        response = self.client.post('/accounts/register/',
                {'username':'o13', 'email':'o13@gmail.com', 'password':'o13$'})
        self.assertEqual(response.status_code, 200)


class LoginViewTesteCase(TestCase):
    def test_if_login_view_returns_200(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code,200)

    def test_if_user_can_login(self):
        response = self.client.post('/accounts/login',
                {'username':'oltjano','password':'test132244'})
        self.assertEqual(response.status_code,200)

