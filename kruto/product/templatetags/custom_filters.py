
from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words=12):
    words = value.split()
    if len(words) > num_words:
        return ' '.join(words[:num_words]) + '...'
    return value
