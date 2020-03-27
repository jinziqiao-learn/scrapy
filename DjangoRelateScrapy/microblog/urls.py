# Author:blue
from django.urls import path
from . import views

app_name = 'microblog'

urlpatterns = [
    path('', views.weibo, name='weibo'),
    path('detail/<int:num>/', views.detail, name='detail'),
]
