# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from books.models import *

# 下面我们演示上下文在 django 中的使用方法
from django.template import loader, RequestContext


def search_form(request):
    return render_to_response('search_form.html')


def search(request):

    # 这里是我们不使用模板进行练习
    # if 'q' in request.GET:
    #     message = 'here is {}'.format(request.GET.get('q'))
    # else:
    #     message = 'nothing happend ..'
    # return HttpResponse(message)
    # return render_to_response('search_form.html')

    # 这里使用模板
    errors = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        if not query:
            errors.append('please enter some characters')
        elif len(query) > 10:
            errors.append('please enter at most 10 characters')
        else:
            books = Book.objects.filter(title__icontains=query)
            return render_to_response('search_results.html', {'books': books, 'query': query})
    return render_to_response('search_form.html', {'errors': errors})


# 演示由下面几个演员联袂出演
def custom_proc(request):
    ''' 该方法就是设置上下文早先具有的一些初始变量 '''

    return {
        'app': 'future',
        'user': request.user,
        'ip_addr': request.META['REMOTE_ADDR'],
    }


def test1(request):
    t = loader.get_template('test1.html')
    c = RequestContext(request, {'message': 'I\'m test1 html'}, processors=[custom_proc])
    return HttpResponse(t.render(c))


def test2(request):
    return render_to_response('test2.html',
        {'message': '<p>I\'m test2 html 2 &lt 3</p>'},
        context_instance=RequestContext(request, processors=[custom_proc])
    )


def img(request):
    ''' 分享静态文件 '''

    img = open('/home/jovi/pra/python/django/archer/books/static/ib.png').read()
    return HttpResponse(img, content_type='image/png')


# 下面是 python 生成 csv 的例子
import csv

UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]


def unruly_passengers_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response


# 下面是 python 生成 pdf 的例子
from reportlab.pdfgen import canvas

def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


# 同样的 pdf 例子 但这里使用到的库更加高效
from cStringIO import StringIO


def hello_pdf2(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = StringIO()

    # Create the PDF object, using the StringIO object as its "file."
    p = canvas.Canvas(temp)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the StringIO buffer and write it to the response.
    response.write(temp.getvalue())
    return response
