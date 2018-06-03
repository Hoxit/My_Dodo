# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkToday
from django import forms
# Create your views here.




# def detail(request):
#     latest_work_list = WorkToday.objects.all()
#     query_list = latest_work_list.values('id','discribe','user')
#     get_data = request.GET['send_form']
#     context = {
#         'work': query_list,
#          'message': get_data,
#          }
#     return render(request, 'todo_app/detail.html', context)

# class detail(ListView):
#     queryset = WorkToday.objects.all()
#     context_object_name = 'work'
#     template_name = 'todo_app/detail.html'

class WorkList(ListView):
    model = WorkToday
    paginate_by = 2


class WorkView(DetailView):
    model = WorkToday


class WorkCreate(CreateView):
    model = WorkToday
    fields = ['discribe', 'pub_date', 'Short_discribre']
    success_url = reverse_lazy('todo_app:work_list')


class WorkUpdate(UpdateView):
    model = WorkToday
    fields = ['discribe', 'pub_date', 'Short_discribre']
    success_url = reverse_lazy('todo_app:work_list')


class WorkDelete(DeleteView):
    model = WorkToday
    success_url = reverse_lazy('todo_app:work_list')


# def index(requset):
#     latest_work_list = WorkToday.objects.all()
#     context = {'latest_work': latest_work_list}
#     return render(requset, 'todo_app/index.html',context)
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
