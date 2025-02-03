from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    fields = ('first_name', 'last_name', 'birth_date', 'images', 'phone_number', 'grade', 'gender', 'enrollment_date')
    success_url = reverse_lazy('student_list')


class StudentUpdatedView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    fields = ('first_name', 'last_name', 'birth_date', 'images', 'phone_number', 'grade', 'enrollment_date')
    success_url = reverse_lazy('student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'students'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/list.html'
    success_url = reverse_lazy('student_list')
