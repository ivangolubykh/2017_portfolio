from django.test import TestCase
from django.core.urlresolvers import reverse


class TestMainPage(TestCase):

    def test_main_page(self):
        """
        """
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
