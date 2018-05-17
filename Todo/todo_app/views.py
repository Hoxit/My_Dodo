# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorkToday , InputForm
# Create your views here.

def index(requset):
    latest_work_list = WorkToday.objects.all()
    context = {'latest_work': latest_work_list}
    return render(requset, 'todo_app/index.html',context)


def detail(request):
    latest_work_list = WorkToday.objects.all()
    query_list = latest_work_list.values('id','discribe')
    get_data = request.GET['send_form']
    context = {'work': query_list, 'message': get_data}
    return render(request, 'todo_app/detail.html', context)


def form(request):
    if request.method == 'GET':
        form = InputForm(request.GET)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = InputForm()
    return render(request, 'todo_app/form.html', {'form': form})

def search_form(request):
    return render(request, 'todo_app/search_form.html')
