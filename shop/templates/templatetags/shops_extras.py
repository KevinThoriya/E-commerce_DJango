from django import template
register = template.Library()

@register.filter(is_safe= True)
def multiply(qty , unit_prize , *arg , **kwargs):
    return qty * unit_prize


