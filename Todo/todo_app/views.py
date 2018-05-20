# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorkToday
from django import forms
# Create your views here.


def index(requset):
    latest_work_list = WorkToday.objects.all()
    context = {'latest_work': latest_work_list}
    return render(requset, 'todo_app/index.html',context)


def detail(request):
    latest_work_list = WorkToday.objects.all()
    query_list = latest_work_list.values('id','discribe','user')
    get_data = request.GET['send_form']
    context = {
        'work': query_list,
         'message': get_data,
         }
    return render(request, 'todo_app/detail.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
