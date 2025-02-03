from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'


class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/form.html'
    fields = ('name', 'teacher', 'subject')
    success_url = reverse_lazy('groups_list')


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'groups/form.html'
    fields = ('name', 'teacher', 'subject')
    success_url = reverse_lazy('groups_list')


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'groups'


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'