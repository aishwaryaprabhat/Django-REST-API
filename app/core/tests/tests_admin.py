from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="aish@gmail.com",
            password="testpassword"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="aish2@gmail.com",
            password="testpassword",
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  #reverse takes care of the URL even if we change it
        res = self.client.get(url)  # performs http get on the url

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


