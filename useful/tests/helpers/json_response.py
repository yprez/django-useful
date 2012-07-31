import datetime
import json

from django.test import TestCase
from django.http import HttpResponse

from useful.helpers import json_response, jsonp_response


class JsonReponseTestCase(TestCase):
    data = {
        'dict': {
            'a': 'b',
            'c': 'd',
            'e': {'nested': 'dict'},
            'f': ['list', 'as', 'value'],
            'g': ['mixing', {'value': 'types'}],
            'e': u'unicode string',
        },
        'null': None,
        'list': [1, 2, 'a', 'b'],
        'with_time': {'a': 'b', 'time': datetime.datetime.now()}
    }

    def test_json_response(self):
        response = json_response(self.data['dict'])

        self.assertIsNotNone(response)

        self.assertIsInstance(response, HttpResponse)

        self.assertIsNotNone(response.content)
        self.assertIsInstance(response.content, str)

        self.assertEquals(json.loads(response.content), self.data['dict'])

        self.assertEquals(response.status_code, 200)

    def test_list_json_response(self):
        response = json_response(self.data['list'])

        self.assertIsNotNone(response.content)
        self.assertIsInstance(response.content, str)

        self.assertEquals(json.loads(response.content), self.data['list'])

    def test_null_json_response(self):
        response = json_response(self.data['null'])

        self.assertIsNotNone(response.content)
        self.assertIsInstance(response.content, str)

        self.assertEquals(json.loads(response.content), self.data['null'])

    def test_json_response_code(self):
        response = json_response(self.data['null'], status=400)
        self.assertEquals(response.status_code, 400)

    def test_json_serializer(self):
        dthandler = lambda x: (x.isoformat()
                               if isinstance(x, datetime.datetime) else x)

        typerror = lambda x: json_response(self.data['with_time'])

        self.assertRaises(TypeError, typerror)

        response = json_response(self.data['with_time'], serializer=dthandler)

        # Back to datetime object
        t = datetime.datetime.strptime(json.loads(response.content)['time'],
                                       '%Y-%m-%dT%H:%M:%S.%f')

        self.assertEquals(t, self.data['with_time']['time'])


class JsonpReponseTestCase(TestCase):
    """ The same as json_response_test, but can't check the result """

    data = JsonReponseTestCase.data  # Borrow the data from json_response test

    def test_jsonp_response(self):
        response = jsonp_response(self.data['dict'])

        self.assertIsNotNone(response)

        self.assertIsInstance(response, HttpResponse)

        self.assertIsNotNone(response.content)
        self.assertIsInstance(response.content, str)

        self.assertEquals(response.status_code, 200)
