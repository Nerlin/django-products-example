from django import template
from django.template.defaultfilters import floatformat

register = template.Library()


@register.filter()
def format_price(product_price):
    formatted_price_value = floatformat(product_price, 2)
    return f"{formatted_price_value}$"
