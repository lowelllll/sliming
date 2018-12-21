from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class OfflineShop(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=50, unique=True)
    grade = models.IntegerField(default=0) # 평점
    description = models.TextField(null=True, blank=True)
    shop_image = models.ImageField(upload_to='%Y/%m/%d/shop')
    status = models.BooleanField() # 마켓이 오픈되어있는지 아닌지
    offline = models.ManyToManyField(OfflineShop, blank=True)
    online = models.URLField(blank=True)
    instagram_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.name])


class Follow(models.Model):
    """
    follower = 팔로우를 요청한 유저 id
    shop = 팔로우 대상 마켓 id
    """
    requester = models.IntegerField()
    shop = models.IntegerField()

    def __str__(self):
        return self.requester










