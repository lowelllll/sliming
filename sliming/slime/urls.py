from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.add_slime, name='add'),
]
