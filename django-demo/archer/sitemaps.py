# coding: utf-8

from django.contrib.sitemaps import Sitemap
from books.models import Book


class BookSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Book.objects.filter(title='flag')

    def location(self, obj):
        return '/item'
