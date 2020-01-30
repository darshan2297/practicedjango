from django import template

register = template.Library()

def cut1(value,arg):
    return value.replace(arg,'')

register.filter('cut1',cut1)

@register.filter()
def up1(value):
    return value.upper()

@register.filter()
def boldcoffee(value):
    return '<b>%s<b>' %value

# @register.filter()
# def boldcoffee(value):
#     '''Returns input wrapped in HTML  tags'''
#     return '<b>%s</b>' % value