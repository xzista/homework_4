from django import template

register = template.Library()

@register.simple_tag
def active(request, url_name):
    return "active text-white bg-primary" if request.resolver_match.url_name == url_name else "text-white"


@register.filter()
def media_filter(path):
    if path:
        return f'media/{path}'
    return '#'