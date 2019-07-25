from django import forms
from .models import Mapmodel, Memo

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from taggit.forms import *

class MapForm(forms.ModelForm):

    class Meta:
        model = Mapmodel
        fields = ('title', 'content', 'address', 'image', 'tags')
        labels = {
            'title' : '제목', 
            'content' : '내용',
            'address' : '주소',
            'image' : '이미지',
            'tags': '태그', 
        }

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-10'
    helper.layout = Layout( 
        Field('title', css_class='input-sm'),
        Field('content', css_class='input-sm'),
        Field('address', css_class='input-sm'),
        Field('image', css_class='btn-secondary'),
        Field('tags', css_class='input-sm'),
    )


class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('memo',)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'