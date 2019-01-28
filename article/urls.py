# coding=utf-8
from django.conf.urls import url
from article import views

app_name = 'article'

urlpatterns = [
    url(r'^article-column/$', views.article_column, name="article_column"),
    url(r'^rename-article-column/$', views.rename_article_column, name="rename_article_column"),
    url(r'^del-article-column/$', views.del_article_column, name='del_article_column'),
    url(r'^article-post/$', views.article_post, name='article_post'),
]
