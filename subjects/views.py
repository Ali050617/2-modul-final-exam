from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/form.html'
    fields = ('name', 'department', 'description')
    success_url = reverse_lazy('subject_list')


class SubjectUpdatedView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    fields = ('name', 'department', 'description')
    success_url = reverse_lazy('subjects')


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subjects'


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/list.html'
    success_url = reverse_lazy('subjects_list')