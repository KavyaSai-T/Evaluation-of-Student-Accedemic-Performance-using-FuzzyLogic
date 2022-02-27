from django import template

register = template.Library()

@register.filter
def division(value, arg):
    return float(value) / arg
def add(value, arg):
	arg = value + arg
	print(arg)
def subtract(value, arg):
	arg = value - arg
	print(arg)

    