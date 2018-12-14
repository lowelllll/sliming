from django import forms
from .models import Slime

class SlimeForm(forms.ModelForm):
    class Meta:
        model = Slime
        fields = (
            'name', 'price', 'volume', 'kind', 'description', 'img', 'video_link',
        )
        labels = {
            'name': '슬라임 이름',
            'price': '가격',
            'volume': '용량',
            'kind': '종류',
            'description': '상세 내용',
            'img': '사진',
            'video_link': '인스타그램 동영상 게시글 링크',
        }