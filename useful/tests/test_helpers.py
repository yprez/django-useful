from django.test import TestCase
from django.contrib.auth.models import User

from useful.helpers import get_object_or_none
from useful.helpers import json_response

import json


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


class JsonReponseTestCase(TestCase):
    def setUp(self):
        self.data = {
            'dict': {
                'a': 'b',
                'c': 'd',
                'e': {'nested': 'dict'},
                'f': ['list', 'as', 'value'],
                'g': ['mixing', {'value': 'types'}],
                'e': u'unicode string',
            }
        }

    def test_json_response(self):
        response = json_response(self.data['dict'])

        self.assertIsNotNone(response)

        from django.http import HttpResponse
        self.assertIsInstance(response, HttpResponse)

        self.assertIsNotNone(response.content)
        self.assertIsInstance(response.content, str)

        self.assertEquals(json.loads(response.content), self.data['dict'])

        self.assertEquals(response.status_code, 200)