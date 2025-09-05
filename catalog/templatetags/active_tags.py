from django import template

from django.conf import settings

register = template.Library()

@register.simple_tag
def active(request, *url_names):
    current_url_name = request.resolver_match.url_name
    if current_url_name in url_names:
        return "active text-white bg-primary"
    return "text-white"


@register.filter()
def media_filter(path):
    if path:
        return f'{settings.MEDIA_URL}{path}'
    return '#'