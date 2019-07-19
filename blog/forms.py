from django import forms
from .models import Mapmodel

class MapForm(forms.ModelForm):

    class Meta:
        model = Mapmodel
        fields = ('title', 'body', 'address', 'image')
        