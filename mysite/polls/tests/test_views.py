from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class OsobaListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testviews', password='TestUserViews')
        self.client.login(username='testviews', password='TestUserViews')

    def test_osoba_list_view(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'person_list.html')