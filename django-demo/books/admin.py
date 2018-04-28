# coding: utf-8

from django.contrib import admin
from books.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    # 提供可以 like 搜索的字段
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    # 就是最右边的那个过滤器 可以根据需求在元组中添加字段
    list_filter = ('publication_date', 'publisher')
    ordering = ('-publication_date',)
    # 在单条记录的管理界面按照顺序显示字段 当然可以隐藏字段
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # 多对多的字段关系最好的展示方法
    filter_horizontal = ('authors',)
    # 外键关系会使用弹出层展示
    raw_id_fields = ('publisher',)

    # 给予该模型一个逐层深入的导航条 当然只有时间字段能这样做 所以这里不是元组
    date_hierarchy = 'publication_date'


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
