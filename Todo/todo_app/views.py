# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorkToday
# Create your views here.

def index(requset):
    latest_work_list = WorkToday.objects.all()
    context = {'latest_work': latest_work_list}
    return render(requset, 'todo_app/index.html',context)


def detail(request):
    latest_work_list = WorkToday.objects.all()
    context = {'work': latest_work_list}
    return render(request, 'todo_app/detail.html', context)
