from django.test import TestCase
from django.contrib.auth.models import User

from useful.helpers import get_object_or_none


class GetObjectOrNoneTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test',
                                        email='test@example.com')

    def test_get_object(self):
        user = get_object_or_none(User, username='test')
        self.assertIsNotNone(user)
