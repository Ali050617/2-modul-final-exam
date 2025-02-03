from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/form.html'
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'address',
              'department', 'subjects', 'qualification', 'join_date', 'employment_type')
    success_url = reverse_lazy('teacher_list')


class TeacherUpdatedView(UpdateView):
    model = Teacher
    template_name = 'teachers/form.html'
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'department', 'subjects', 'qualification',
              'join_date', 'employment_type')
    success_url = reverse_lazy('teacher_list')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teachers'


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/list.html'
    success_url = reverse_lazy('teacher_list')
