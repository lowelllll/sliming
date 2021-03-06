import re
from django.db import models
from shop.models import Shop
from django.forms import ValidationError

def instagram_post_url_validator(url):
    if not re.match(r'^https://www.instagram.com/p/.', url):
        if not re.match(r'^https://scontent-icn1-1.cdninstagram.com/.', url):
            raise ValidationError('인스타그램 게시글 링크는 https://www.instagram.com/p/ 로 시작되는 링크여야합니다.')


class Kind(models.Model): # 슬라임 종류
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Slime(models.Model): # 슬라임 상품
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=100) # 슬라임 이름
    price = models.IntegerField()
    volume = models.IntegerField() # 용량
    kind = models.ForeignKey(Kind) # 슬라임 종류
    description = models.TextField() # 슬라임 정보
    img = models.ImageField(upload_to='%Y/%m/%d/slime')
    video_link = models.URLField(validators=[instagram_post_url_validator])
    status = models.IntegerField() # 슬라임 상품의 상태 (1: 판매중, 2: 판매 중단, 3: 판매 임시 중단)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Review(models.Model): # 슬라임 리뷰
    slime = models.ForeignKey(Slime)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='%Y/%m/%d/review')
    video_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

# class SlimeExtra(models.Model): # 슬라임 상품 기타
#     slime = models.ForeignKey(Slime)
#     view = models.IntegerField(default=0)
#     favorite = models.IntegerField(default=0)

