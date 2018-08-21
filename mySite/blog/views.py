# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def readme(request):
    return HttpResponse(u"欢迎使用jayjay的博客")

def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    result = int(a) + int(b)
    return HttpResponse(str(result))

def home(request):
    #showmessage = {u"大家好":"num1",u"我是渣渣辉":"num2",'nihao':"num3"}
    showmessage = ['num1','num2','num3','num4']
    return render(request,'blog/home.html',{'showmessage':showmessage})