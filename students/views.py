from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

# 显示学生信息
from django.urls import reverse

from students.models import Student

# 学生信息展示页
def student_list(request):
    student_list = Student.objects.all()
    return render(request,'students/student.html',locals())
    # return redirect(reverse("students:index"))

# 学生个人信息展示页
def stu_message(request,id):
    # return HttpResponse("你真帅")
    student = Student.objects.get(id=id)
    return render(request,'students/stu_message.html',locals())

# 反向解析的函数
def index(request):
    return render(request,'students/index.html')




