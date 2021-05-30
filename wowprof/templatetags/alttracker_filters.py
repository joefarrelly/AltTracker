from django import template
import datetime
from django.utils import timezone

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
    if isinstance(value, str):
        return (value)
    else:
        time = timezone.now() - value
        if time.days >= 1:
            return (str(time.days) + " day(s) ago")
        elif time.seconds >= 3600:
            return (str(int((time.seconds / 60) / 60)) + " hour(s) ago")
        elif time.seconds >= 60:
            return (str(int(time.seconds / 60)) + " minute(s) ago")
        return ("Less than a minute ago")
