from django.contrib.auth.models import User
from django.test import TestCase, Client, TransactionTestCase


# Create your tests here.
class UserHistoryTest(TransactionTestCase):
    self.user = User.objects.create(username='testuser', password='testpass', email='test@test.com')
    self.client = Client()

    def test_history(self):
        self.client.login(username=self.user.username, password='testpass')
        # get_history function having login_required decorator
        response = self.client.post(reverse('get_history'), {'user_id': self.user.id})
        self.assertEqual(response.status_code, 200)
