from django import forms
from .models import Mapmodel, Memo


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

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('memo',)