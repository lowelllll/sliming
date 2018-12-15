from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail_slime, name='detail'),
    url(r'^add/$', views.add_slime, name='add'),
    url(r'^modify/(?P<id>\d+)/$', views.modify_slime, name='modify'),
]
