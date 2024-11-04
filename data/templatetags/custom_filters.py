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
    # Assuming 'value' is a datetime object
    local_tz = pytz.timezone('Asia/Yangon')  # Replace with your desired timezone
    gmt630_time = value.astimezone(local_tz)
    return gmt630_time.strftime('%b %d, %Y, %I:%M %p')  # Format as needed
register.filter('convert_to_gmt630',convert_to_gmt630)