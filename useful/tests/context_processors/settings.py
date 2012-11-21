from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class SettingsContextProcessorTestCase(TestCase):
    urls = 'useful.tests.test_urls'

    def setUp(self):
        self.client = Client()

    def test_context_processor(self):
        # unrelated view, but it shouldn't matter
        url = reverse('test_extra_context_view_no_context')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('settings' in response.context)

        template_settings = response.context.get('settings')

        self.assertEqual(settings, template_settings)

    def test_context_processor_in_template(self):
        # unrelated view, but it shouldn't matter
        settings.ARBITRARY_VALUE = 'TEST_VALUE'  # modify settings on the fly
        url = reverse('test_extra_context_view_no_context')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('TEST_VALUE', response.content)
