from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from microblog.models import HotSpot


def weibo(request):
    return render(request, 'weibo.html')


def detail(request, num):
    list = HotSpot.objects.all()
    paginator = Paginator(list, 8)
    if num > 100:
        num = 1
    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page})


