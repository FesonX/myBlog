# coding=utf-8
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'
urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'),
        name='user_login'),
    url(r'^new-login/$', auth_views.auth_login, {'template_name': 'account/login.html'}),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logout.html'),
        name='user_logout'),
    url(r'^register/$', views.register, name='user_register'),
]

