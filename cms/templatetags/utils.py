from django import template

register = template.Library()


@register.filter(name="multiply")
def multiply(value, args):
    return value * args
