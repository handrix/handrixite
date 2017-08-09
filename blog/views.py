# -*- coding:utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from . import models
import markdown2


class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = models.Article.objects.all()
        return article_list
        pass

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = models.Category.objects.all().order_by('name')
        kwargs['tag_list'] = models.Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
        pass
    pass


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_queryset(self):
        article_list = models.Article.objects.all()
        return article_list
        pass

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj
        pass
    pass


class CategoryView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = models.Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        for article in article_list:
            article.body = article.body
        return article_list
        pass

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = models.Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)
        pass
    pass


class TagView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = models.Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        for article in article_list:
            article.body = article.body
        return article_list
        pass

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = models.Tag.objects.all().order_by('name')
        return super(TagView, self).get_context_data(**kwargs)
        pass
    pass


class AboutMeView(TemplateView):
    template_name = "blog/about.html"