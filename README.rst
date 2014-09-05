=============
django-useful
=============

A collection of reusable Django snippets.

**Warning:** This project is not longer actively supported.
Most of the functionallity isn't needed with newer versions of Django.


**Travis CI build status:** |travis-ci-status|


**Work in progress**:
Currently this package is still under development, and intended mainly for my
personal use. New features will be added gradually.

Unlike other similar packages, I'll try to keep it fully tested, documented,
and compatible with several Django and Python versions.

**Compatible with:**

* **Python:** 2.6, 2.7, 3.3 and 3.4
* **Django:** 1.3, 1.4, 1.5, 1.6 and 1.7
* **Celery:** 2.5, 3.0 and 3.1 *(optional)*

Installation
------------

Install by using pip or easy_install::

  pip install django-useful

Or install from source::

    git clone git@github.com:yprez/django-useful.git
    cd django-useful
    python setup.py install

To add this application into your project, just add it to your
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'useful',
    )


------------


For more details, see the `Documentation`_.


.. _`Documentation`: http://django-useful.rtfd.org/

.. |travis-ci-status| image:: https://secure.travis-ci.org/yprez/django-useful.png?branch=master
   :target: http://travis-ci.org/yprez/django-useful
