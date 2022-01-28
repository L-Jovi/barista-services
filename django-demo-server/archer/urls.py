# coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from archer.views import *
# 这里报红因为没用到 原因就是我们在下面使用了更加面向对象的方法去导入每个应用 app 的后台逻辑
from books import views as books_views
from contact import views as contact_views

# 这里在 index 页面增加 feeds
from archer.feeds import LatestEntries

# 增加 sitemaps
from django.contrib.sitemaps.views import sitemap
from archer.sitemaps import BookSitemap


sitemaps = {
    'index': BookSitemap,
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 结合上方的 feeds 字典联合标识 url >>> /feed/latst/ 和 /feed/categories/
    url(r'^feed/$', LatestEntries()),

    # sitemaps
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # django 自带的后台管理应用 很厉害哦
    url(r'^admin/', include(admin.site.urls)),

    # 我们的一些小练习
    url(r'^index/$', index),
    url(r'^cur_time/(\d{1,2})$', cur_time),

    # 简单的模板查看 request 对象的 META 字典内容
    url(r'^display_meta/$', display_meta),

    # 表单的练习
    # 最后一次改进 我们吧表单的提交展示放在了同一张页面中
    # url(r'^search-form/$', views.search_form),
    url(r'^search/$', books_views.search),

    # 这里是使用 include 的测试用例
    url(r'^test/', include('books.urls')),

    # >>> 下面的方法都被再下面的前缀代替了 我保留前后的历史以便进行对比
    # 联系人的处理 这里把后台逻辑单独做了一个包 因为跟其他模块耦合性低
    # url(r'^contact/$', contact_views.contact),
    # 用不同的方法跳转 这里直接使用字符串形式导入了模块
    # url(r'^happend/$', 'contact.views.happend'),
)


# 更加高端的方法是前缀混用 一看你就明白了
# 这里为了增加趣味性 我们提供了关键字参数 说穿了就是直接在 url 这里决定参数值 这主要为了相同后台逻辑复用
urlpatterns += patterns('contact.views',
    url(r'^contact/$', 'contact'),
    url(r'^foo/(?P<count>\d+)/$', 'foobar', {'name': 'archer'}),
    url(r'^bar/(?P<count>\d+)/$', 'foobar', {'name': 'saber'}),
)


# 这里有些更好玩的东西 如果你想做一些调试的逻辑展示一些仅在开发阶段才能出现的页面就可以这样
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debug/$', 'debug'),
    )
