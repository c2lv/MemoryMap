from django import forms
from .models import Mapmodel, Memo

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MapForm(forms.ModelForm):

    class Meta:
        model = Mapmodel
        fields = ('title', 'content', 'address', 'image')
        labels = {
            'title' : '제목', 
            'content' : '내용',
            'address' : '주소',
            'image' : '이미지',
        }

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'


class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('memo',)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'