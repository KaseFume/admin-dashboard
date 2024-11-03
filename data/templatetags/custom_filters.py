from django import template

register = template.Library()

def extract_number(product_id):
    try:
        return product_id.split('-')[1]
    except IndexError:
        return ''

register.filter('extract_number',extract_number)