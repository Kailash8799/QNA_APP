from django import template

register = template.Library()

@register.filter(name='splitstring')
def splitstring(array):
    print(array)