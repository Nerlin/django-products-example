from django.forms import Widget
from django.forms.renderers import TemplatesSetting


class PriceWidget(Widget):
    template_name = "django/forms/widgets/price.html"

    def render(self, name, value, attrs=None, renderer=None):
        renderer = TemplatesSetting()
        '''
        Overriding renderer to TemplatesSetting extremely important. 
        Without this Django can't find our custom template.
        '''
        return super().render(name, value, attrs, renderer)
