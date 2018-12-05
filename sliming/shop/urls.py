from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create_shop, name='create'),
    url(r'^detail/(?P<shop>\w+)/$', views.detail_shop, name='detail'),
]