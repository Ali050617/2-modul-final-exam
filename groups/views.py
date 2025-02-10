from django.contrib import messages
from .models import Group
from .forms import GroupForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
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
    success_url = reverse_lazy('groups:groups_list')

    def form_valid(self, form):
        print("form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_valid(form)

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:groups_list')

    def form_valid(self, form):
        messages.success(self.request, "Group successfully updated!")
        return super().form_valid(form)


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'groups'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:groups_list')

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return redirect(self.success_url)