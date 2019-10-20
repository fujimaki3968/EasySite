from django import template

register = template.Library()


@register.filter(name="multiplie")
def multiplie(value, args):
	return value * args
