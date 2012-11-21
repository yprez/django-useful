from django.conf import settings as django_settings


def settings(request):
    """
    Settings context processor
    Allows access to project settings from the templates
    """
    return {'settings': django_settings}
