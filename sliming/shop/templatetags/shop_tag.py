from django import template

register = template.Library()

# shop에 관련된 템플릿 태그

# @register.filter
# def in_category(things, category):
#     return things.filter(category=category)
#
# {% for category in categories %}
#   {% for thing in things|in_category:category %}
#     {{ thing }}
#   {% endfor %}
# {% endfor %}

@register.filter
def count(slimes):
    return slimes.filter(status=1).count()