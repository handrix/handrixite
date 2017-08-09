# -*- coding:utf-8 -*-

from django.db import models


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=80)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    body = models.TextField()
    author = models.CharField(max_length=20)
    photo = models.URLField(blank=True, default="http://placehold.it/900x300")
    create_data = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    pass

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_data']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
