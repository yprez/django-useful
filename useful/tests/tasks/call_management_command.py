from django.test.simple import DjangoTestSuiteRunner

from celery.task import Task

from useful.tasks import call_management_command


class ManagementCommandTestCase(DjangoTestSuiteRunner):
    """Test calling a management command as a Celery task"""
    def setup_test_environment(self, **kwargs):
        # Monkey-patch Task.on_success() method
        def on_success_patched(self, retval, task_id, args, kwargs):
            DatabaseBackend().store_result(task_id, retval, "SUCCESS")

        def on_failure_patched(self, exc, task_id, args, kwargs, einfo):
            DatabaseBackend().store_result(task_id, exc, "SUCCESS")

        Task.on_success = classmethod(on_success_patched)
        Task.on_failure = classmethod(on_failure_patched)

    def test_success(self):
        t = call_management_command.delay('validate')
        self.assertEquals(t.status, 'SUCCESS')

    def test_failure(self):
        with self.settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=False):
            t = call_management_command.delay('somethingrandomthatdoesntexist')
            self.assertEquals(t.status, 'FAILURE')

    def test_name(self):
        self.assertEquals(call_management_command.name,
                          'call_management_command')
