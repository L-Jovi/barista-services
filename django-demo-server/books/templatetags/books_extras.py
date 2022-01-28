# coding: utf-8

from django import template

register = template.Library()


def cut(value, arg):
    ''' 我们写一个自定义的过滤器吧 作用就是去掉空格好了 '''

    return value.replace(arg, '')


@register.filter(name='low')
def lower(value):
    return value.lower()


# 用下面的方法注册我们自己的过滤器
register.filter('cut', cut)
