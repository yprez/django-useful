#!/bin/sh
pip install .. --upgrade  # Update the version of django-useful
python manage.py test useful -v2
