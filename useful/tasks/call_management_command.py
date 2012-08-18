from celery.task import task
from django.core import management


@task()
def call_management_command(command):
    """
    Run a management command as a Celery task.

    Useful for running periodic management commands with Celerybeat.
    """

    management.call_command(command)
