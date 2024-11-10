from django import template
from django.utils import timezone
import pytz
register = template.Library()

def extract_number(product_id):
    try:
        return product_id.split('-')[1]
    except IndexError:
        return ''

register.filter('extract_number',extract_number)

def convert_to_gmt630(value):
    if not value:
        return ''
    # Assuming 'value' is a naive datetime object (without timezone info)
    # or aware datetime object (with timezone info)
    if timezone.is_aware(value):
        # If the datetime is already timezone-aware, convert it to the desired timezone
        local_tz = pytz.timezone('Asia/Yangon')
        gmt630_time = value.astimezone(local_tz)
    else:
        # If it's naive, assume it's in UTC and localize it to the desired timezone
        local_tz = pytz.timezone('Asia/Yangon')
        gmt630_time = local_tz.localize(value)

    return gmt630_time.strftime('%b %d, %Y, %I:%M %p')   # Format as needed
register.filter('convert_to_gmt630',convert_to_gmt630)

@register.filter
def subtract(value, arg):
    return value - arg