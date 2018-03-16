from django.conf.urls import url

from students.views import student_list,stu_message,index

urlpatterns = [
    url(r'^student_list/$',student_list,name='student_list'),
    url(r'^stu_message/(?P<id>\d+)/$',stu_message,name='stu_message'),
    url(r'^index/$',index,name='index')
]