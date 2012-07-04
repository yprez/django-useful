from django.http import HttpResponse

try:
    import simplejson as json
except:
    import json


def json_response(data, status=200, serializer=None):
    return HttpResponse(json.dumps(data, default=serializer),
                        status=status,
                        content_type='application/json; charset=UTF-8')


def jsonp_response(data, callback="f", status=200, serializer=None):
    ret = "{callback}('{val}');".format(callback=callback,
                                    val=json.dumps(data, default=serializer))

    return HttpResponse(ret,
                        status=status,
                        content_type='application/x-javascript; charset=UTF-8')
