from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def referer(context, fallback_url, *args):
    request = context["request"]
    url = request.GET.get("next")
    if not url:
        try:
            url = reverse(fallback_url, args=args)
        except NoReverseMatch:
            url = fallback_url

    if not url:
        url = request.META.get("HTTP_REFERER")
    return url


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    request = context["request"]
    get_params = request.GET.copy()
    for field, value in kwargs.items():
        get_params[field] = value
    return get_params.urlencode()


@register.simple_tag(takes_context=True)
def url_referred(context, *args, **kwargs):
    request = context["request"]
    current_path = request.path
    url_name, *params = args
    url = reverse(url_name, args=params)
    return f"{url}?next={current_path}"
