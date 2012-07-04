from django.views.generic import TemplateView


class ExtraContextTemplateView(TemplateView):
    """
    Extension of Django TemplateView CBV that allows adding extra context
    """
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).\
            get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context
