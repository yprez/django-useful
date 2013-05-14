CHANGELOG
=========


0.1.2 - 21/11/2012
------------------

* Settings context processor - allows accessing settings from templates.


0.1.1 - 11/10/2012
------------------

* Bugfix: Task - call_management_command - set task name correctly.
  Was causing problems with some versions of Celery.


0.1.0 - 25/09/2012
------------------

* Initial release.
* Included features:
    * Views: ExtraContextTemplateView
    * Helpers: get_object_or_none, json_response, jsonp_response
    * Tasks: call_management_command
