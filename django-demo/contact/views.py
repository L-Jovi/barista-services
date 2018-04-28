# coding: utf-8

from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from contact.forms import ContactForm


# def contact(request):
#     '''
#     下面的功能杂乱而且难以维护 最大的原因就是我们验证的时候没有使用高级库
#     稍后下面的功能会被 django 的高级库重写
#     '''
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             # 这里用重定向的意义就是不希望用户重复提交 POST 请求
#             return HttpResponseRedirect('/contact/thanks/')
#
#     return render_to_response('contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''),
#     })


def contact(request):
    '''
    这里是通过 django 高级库 forms 实现的验证 代码非常清爽
    '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject': 'my people'}
        )
    return render_to_response('contact_form.html', {'form': form})


def foobar(request, count, name):
    return HttpResponse('sth happend! {} with number {}'.format(name, count))
