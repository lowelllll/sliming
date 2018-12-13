from django import forms
from .models import Slime

class SlimeForm(forms.ModelForm):
    class Meta:
        model = Slime
        fields = ('name', 'price', 'kind', 'description', 'img', 'video_link')

