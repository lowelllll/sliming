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
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    offline = models.ManyToManyField(OfflineShop, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.name])










