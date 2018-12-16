from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=30, null=True, blank=False)
    profile_image = models.ImageField(upload_to='%Y/%m/%d/profile')
    birth_year = models.DateTimeField() # 출생년도 파악

    def __str__(self):
        return self.nickname

    # TODO : 마이페이지, get_absolute_url
