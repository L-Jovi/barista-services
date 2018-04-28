# coding: utf-8

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from books.models import Book


class LatestEntries(Feed):
    title = "My Book"
    link = "/archive/"
    description = "The latest news about stuff."

    def items(self):
        return Book.objects.order_by('-publication_date')[:3]

    def item_title(self, item):
        return item.title

    # def item_description(self, item):
    #     return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        # return reverse('news-item', args=[item.pk])
        return '/news-item'
