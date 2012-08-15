from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class ExtraContextTemplateViewTestCase(TestCase):
    urls = 'useful.tests.test_urls'

    def setUp(self):
        self.client = Client()

    def test_no_context(self):
        url = reverse('test_extra_context_view_no_context')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['test.html'])
        self.assertFalse('extra' in response.context)

    def test_with_context(self):
        url = reverse('test_extra_context_view_w_context')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['test.html'])
        self.assertTrue('extra' in response.context)
