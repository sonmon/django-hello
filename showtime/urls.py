from django.conf.urls import url
from .views import current_time

# 这里是应用的url地址,正则匹配如果加上,在url中就得添加
urlpatterns = [
    url(r'^$',current_time),
]