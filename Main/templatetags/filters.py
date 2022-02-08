from django import template

register = template.Library()


@register.filter(name='range_')
def range_(number):
    return range(number)
