from django.test import TestCase

from useful.tasks import call_management_command


class ManagementCommandTestCase(TestCase):
    """Test calling a management command as a Celery task"""
    def test_success(self):
        t = call_management_command.delay('validate')
        self.assertEquals(t.status, 'SUCCESS')

    def test_failure(self):
        t = call_management_command.delay('somethingrandomthatdoesntexist')
        self.assertEquals(t.status, 'FAILURE')

    def test_name(self):
        self.assertEquals(call_management_command.name,
                          'call_management_command')
