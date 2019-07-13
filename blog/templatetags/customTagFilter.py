from django import template
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
def add_link(item):
    content = item.content

    tags = item.tag_set.all()

    for tag in tags:
        content = re.sub(r'\#'+tag.name+r'\b','<a href="검색URL 추가바람')

    return content