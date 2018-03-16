from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def current_time(request):
    now = datetime.now()
    # return HttpResponse("<h1>It is %s</h1>"%now)
    return render(request,'showtime/current_time.html',{'now':now})