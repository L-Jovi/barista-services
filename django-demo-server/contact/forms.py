# coding: utf-8

from django import forms


class ContactForm(forms.Form):
     subject = forms.CharField(max_length=100)
     # 下面的 label 可以自定义 html 中展示的文字 因为系统默认的有些不太好看
     email = forms.EmailField(required=False, label='e-mail addr')
     # 设置表现的 html 为 textarea
     message = forms.CharField(widget=forms.Textarea)

     # 我们可以自定义一个新的校验规则 比如检查 textarea 中的单词数目不能太少
     def clean_message(self):
         message = self.cleaned_data()['message']
         num_words = len(message.split())
         if num_words < 4:
             raise forms.ValidationError('Not enough words ..')
         return message
