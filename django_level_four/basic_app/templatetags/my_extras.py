from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    this cuts out all the value of 'arg' argument from string

    """
    return value.replace(arg,'')


