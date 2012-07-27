from django.contrib.auth.models import User
from django.test import TestCase

from useful.helpers import get_object_or_none


class GetObjectOrNoneTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test',
                                        email='test@example.com')

    def test_get_object(self):
        user = get_object_or_none(User, username='test')
        self.assertIsNotNone(user)
        self.assertEquals(type(user), type(self.user))
        self.assertEquals(user, self.user)

        user = get_object_or_none(User, email='test@example.com')
        self.assertIsNotNone(user)
        self.assertEquals(type(user), type(self.user))
        self.assertEquals(user, self.user)

    def test_get_none(self):
        user = get_object_or_none(User, username='nonexistent')
        self.assertIsNone(user)

        user = get_object_or_none(User, email='doesnot@exist.com')
        self.assertIsNone(user)
