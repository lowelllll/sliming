from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'shop_image', 'offline']
        widgets = {
            'offline':forms.SelectMultiple,
        }
        labels = {
            'name':'마켓 이름',
            'description' : '설명',
            'shop_image' : '마켓 대표 이미지',
            'offline' : '오프라인 판매처',
        }