from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime


# 定义视图函数
def index(request):
    return render(request, 'hellodjango/hello.html')
    # return HttpResponse("<h1>你好,django</h1>")
