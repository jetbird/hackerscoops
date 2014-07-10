from django.test import TestCase, Client

# Create your tests here.


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
                {'username':'o13', 'email':'o13@gmail.com', 'password':'o13'})
        self.assertEqual(response.status_code, 200)
