# coding: utf-8

from django.conf.urls import patterns, url


urlpatterns = patterns('books.views',
    # 下半部分 url 在这里 完整路由拼起来就好啦
    url('^1/$', 'test1'),
    url('^2/$', 'test2'),
    url('^img/$', 'img'),
    url('^csv/$', 'unruly_passengers_csv'),
    url('^pdf/$', 'hello_pdf'),
    url('^pdf2/$', 'hello_pdf2'),
)
