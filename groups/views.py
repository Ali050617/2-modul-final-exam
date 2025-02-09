from django.contrib import messages
from .models import Group
from .forms import GroupForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups_list')

    def form_valid(self, form):
        messages.success(self.request, "Group successfully created!")
        return super().form_valid(form)


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups_list')

    def form_valid(self, form):
        messages.success(self.request, "Group successfully updated!")
        return super().form_valid(form)


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'groups'


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Group successfully deleted!")
        return super().delete(request, *args, **kwargs)
