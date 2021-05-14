from django import template

register = template.Library()


@register.filter(name='slug')
def slug(value):
    return ((value).replace('\'', '')).lower()
