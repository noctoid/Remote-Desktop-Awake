from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^awake/$', views.awake, name='awake'),
]
