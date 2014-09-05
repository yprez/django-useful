# Django settings for test_project project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

TIME_ZONE = 'Etc/UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

STATIC_URL = '/static/'

SECRET_KEY = 't^4dt#fkxftpborp@%lg*#h2wj%vizl)#pkkt$&amp;0f7b87rbu6y'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test_project.urls'
WSGI_APPLICATION = 'test_project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.admin',

    'djcelery',
    'django_nose',

    'useful',  # Import the app to run tests
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

TEMPLATE_CONTEXT_PROCESSORS = (
    'useful.context_processors.settings',
)

BROKER_BACKEND = 'memory'
CELERY_ALWAYS_EAGER = True

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'cleanup': {
        'task': 'useful.tasks.call_management_command',
        'schedule': timedelta(seconds=10),
        'args': ('validate', ),
    },
}
