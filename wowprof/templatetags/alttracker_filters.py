from django import template
import datetime
from django.utils import timezone
from wowprof.lib.custom import date_diff_format

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


@register.filter(name='datediff')
def datadiff(value):
    return (date_diff_format(value))


@register.filter(name='goldcount')
def goldcount(value):
    if value == '':
        return ('---')
    else:
        return (f'{int(int(value) / 10000):,}')
