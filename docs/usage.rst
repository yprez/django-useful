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

...

jsonp_response
--------------

.. autofunction:: useful.helpers.jsonp_response

...



Views
=====

...
