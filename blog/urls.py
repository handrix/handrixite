# -*- coding:utf-8 -*-

from django.conf.urls import url
from .views import IndexView, BlogDetailView, CategoryView, TagView, AboutMeView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutMeView.as_view(), name='about'),
    url(r'^article/(?P<article_id>\d+)$', BlogDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', TagView.as_view(), name='tag'),
]