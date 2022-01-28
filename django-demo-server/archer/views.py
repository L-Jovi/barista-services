# coding: utf-8

import datetime
from django.utils.translation import ugettext as _

from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template

# replace overhead 3 libs
from django.shortcuts import render_to_response


def index(request):
    ''' 标记可以国际化的字符串 '''

    output = _('Welcome to jovi\'s home ..')
    return HttpResponse(output)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def cur_time(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()

    now = datetime.datetime.now()

    # now load template
    # tem = Template('<html><body>now number {{ num }} time is {{ now | date:"F - j - Y" }} </body></html>')
    # tem = get_template('cur_time.html')

    # htm = '<html><body>now number {} time is {} </body></html>'.format(num, now)
    # htm = tem.render(Context({'num': num, 'now': now}))

    # return HttpResponse(htm)

    # more simple way to load template
    # return render_to_response('cur_time.html', {'num': num, 'now': now})

    # you could use locals to map local key and value
    # return render_to_response('apps/cur_time.html', locals())
    # return render_to_response('index.html', locals())
    return render_to_response('apps/extend_base2.html', locals())
