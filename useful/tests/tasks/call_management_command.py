from django.test import TestCase

from useful.tasks import call_management_command


class ManagementCommandTestCase(TestCase):
    """Test calling a management command as a Celery task"""
    def test_management_command(self):
        t = call_management_command.delay('validate')
        self.assertEquals(t.status, 'SUCCESS')
