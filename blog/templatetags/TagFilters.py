from django import template
from django.urls import reverse
import re

"""
사용자 정의 필터
태그 사용법
1. template 상단에 {% load customTagFilter %}
문구를 넣어 해당 필터를 로드한다.
2. Article의 content(본문)을 가져오는 경우 {{ article|add_link|safe }}
3. 클릭시 URL은 검색 혹은 태그 관련된 URL을 사용


"""

register = template.Library()

@register.filter
def add_link_to_hashtag(item):
    content = item.content

    tags = item.tags.all()

    for tag in tags:
        content = re.sub(r'\#'+tag.name+r'\b','<a href="검색URL 추가바람')

    return content


@register.filter
def add_link_to_tag(item):
    tag_string = []
    tags = item.tags.all()

    str_start = "<form method='GET' action=\"{url}\">".format(url = reverse("blog:search"))
    for tag in tags:
        # temp = '''<button type="button" value="{name}">{name}</button>'''.format(name=tag.name)) 
        # temp = '''<a href="{url}">{name}</a>'''.format(name=tag.name, url = reverse("blog:search", kwargs={'tag':tag.name}))
        temp = '''<a href="{url}">{name}</a>'''.format(name=tag.name, url = reverse("blog:search"))
        tag_string.append(temp)
    str_end = "</form>"

    return str_start + ", ".join(tag_string) + str_end