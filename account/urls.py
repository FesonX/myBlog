# coding=utf-8
from django.conf.urls import url
from django.conf import settings
from . import views

app_name='account'
urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
]

