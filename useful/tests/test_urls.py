from django.conf.urls import url, patterns

from useful.views import ExtraContextTemplateView

urlpatterns = patterns('',
    url(r'^test_extra_context_view_no_context$',
        ExtraContextTemplateView.as_view(template_name='test.html'),
        name='test_extra_context_view_no_context'),

    url(r'^test_extra_context_view_w_context$',
        ExtraContextTemplateView.as_view(template_name='test.html',
                                         extra_context={'extra': 'context'}),
        name='test_extra_context_view_w_context'),
)
