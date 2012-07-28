=====
Usage
=====

Helpers
=======

get_object_or_none
------------------

.. autofunction:: useful.helpers.get_object_or_none

**Sample usage:**
::

    from django.contrib.auth.models import User
    from useful.helpers import get_object_or_none

    user = get_object_or_none(User, username='test')

    if not user:
        pass  # ... do something

While withouth the shortcut you would do something like::

    try:
        user = User.objects.get(username='test')
    except User.does_not_exist:
        user = None

This also simplifying more advanced cases::

    user = get_object_or_none(SomeModel, field='value1') \
            or get_object_or_none(SomeModel, field='value2')


json_response
-------------

.. autofunction:: useful.helpers.json_response

**Sample usage:**
::
    # views.py
    from useful.helpers import json_response

    def some_view(request):
        data = {'a': 'b', 'key': 'value'}

        return json_response(data)  # Returns an HttpResponse object
                                    # With `data` encoded as json.

Return a different status code::

    # views.py
    from useful.helpers import json_response

    def some_view(request):
        return json_response(data={
            'status': 'error',
            'message': 'something terrible happened!',
        }, status=500)

Or use a custom JSON serializer::

    # views.py
    import datetime
    from useful.helpers import json_response

    def some_view(request):
        data = {'date': datetime.datetime.now()}

        dthandler = lambda x: (x.isoformat()
                               if isinstance(x, datetime.datetime) else x)

        return json_response(data, serializer=dthandler)


jsonp_response
--------------

.. autofunction:: useful.helpers.jsonp_response

Usage is the same as `json_response`_


Views
=====

...
