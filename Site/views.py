from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms

# Create your views here.

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 100)
	mail = forms.EmailField()
	namber = forms.IntegerField()

def index(requset):
    return render(requset,'Site/index.html')

def about(requset):
    return render(requset,'Site/about.html')

def contact(requset):
    return render(requset,'Site/contact.html')

def progect(requset):
    return render(requset,'Site/progect.html')

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            namber = form.cleaned_data['namber']

            recepients = ['n.snov@outlook.com']

            msg = "здавствуйте, мое имя "+ name + ". Вот мои контактные данные: телефон - "+ str(namber) + " и e-mail - "+ mail
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            try:
                send_mail("свяжитесь со мной", msg, 'sforogon2@mail.ru', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/')