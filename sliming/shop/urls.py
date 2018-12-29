from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create_shop, name='create'),
    url(r'^$', views.list_shop, name='list'),
    url(r'^list/$', views.more_shops, name='more_list'),
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^(?P<shop>\w+)/$', views.detail_shop, name='detail'), # 마지막에 둬야함. url 찾지 못함
]