from django import template

register = template.Library()


@register.filter(name='slug')
def slug(value):
    return ((value).replace('\'', '')).lower()


@register.filter(name='display')
def display(value):
    return ((value).replace('_', ' ')).title()


@register.filter(name='cssname')
def cssname(value):
    return ((value).replace('_', '-')).lower()
