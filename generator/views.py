import random
from django.shortcuts import render
from django.http import HttpResponse
from regex import R
from sympy import RR, re
# Create your views here.


def password(request):
    print(request.GET)

    length = request.GET['lenghth']
    input_lenghth = request.GET['input-lenghth']
    lenghth = input_lenghth if input_lenghth else length
    # a~z
    password_word = [chr(i) for i in range(97, 123, 1)]
    print(password_word)
    # 大寫
    if request.GET.get('uppercase') == 'on':
        password_word += [chr(i) for i in range(65, 91, 1)]
    # 數字
    if request.GET.get('number') == 'on':
        password_word += [chr(i) for i in range(48, 58, 1)]
    # 特殊
    if request.GET.get('special') == 'on':
        password_word += [chr(i) for i in range(33, 48, 1)]
    password = ''.join([random.choice(password_word)
                        for i in range(eval(lenghth))])
    return render(request, 'password.html', locals())


def index(request):

    return render(request, 'index.html', locals())
