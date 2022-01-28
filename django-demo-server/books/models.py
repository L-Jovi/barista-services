# coding: utf-8

from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['address']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    # 写一些自定义的方法 理解模型内的定制
    def _get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    # 这里比较特殊的一点是又将方法进一步封装为属性 表现出来更加对象化
    full_name = property(_get_full_name)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class BookManager(models.Manager):
    ''' 可以随时添加额外的 manager 为表增加自定义的 orm 方法 '''

    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


from django.contrib.sitemaps import ping_google


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    # num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' 在模型中定义一个可以通知 google 重新索引自己的方法 '''

        super(Book, self).save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass
