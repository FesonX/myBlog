"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from django.contrib.sitemaps import GenericSitemap
from article.models import ArticlePost


info_dict = {
    'queryset': ArticlePost.objects.all(),
    'date_field': 'created',
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^sitemap\.xml$', views.sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.8)}},
        name='django.contrib.sitemaps.views.sitemap'),
    # Using app_name with include is deprecated in Django 1.9
    # and does not work in Django 2.0. Set app_name in account/urls.py instead
    # url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^account/', include('account.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^image/', include('image.urls')),
    url(r'^about$', TemplateView.as_view(template_name="about.html"), name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
