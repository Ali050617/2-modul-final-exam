from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


class DepartmentsCreateView(CreateView):
    model = Department
    template_name = 'departments/form.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('depart_list')


class DepartmentsUpdateView(UpdateView):
    model = Department
    template_name = 'departments/form.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('depart_list')


class DepartmentsDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'departments'


class DepartmentsDeleteView(DeleteView):
    model = Department
    template_name = 'departments/list.html'
    success_url = reverse_lazy('depart_list')


