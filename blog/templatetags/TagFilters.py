from django import template
from django.urls import reverse
from django.shortcuts import resolve_url 
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

    for tag in tags:
        # url = "/blog/search"
        url = resolve_url("blog:search")
        # url = url[:len(url)-1]
        # temp = '''<form method="GET" action="{url}"><input type="submit" name="search" value="{name}"></form>'''.format(name=tag.name, url=url)
        temp = '''<a href="{url}?target={name}">{name}</a>'''.format(name=tag.name, url=url)
        tag_string.append(temp)

    return ", ".join(tag_string) 