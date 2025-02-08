from .models import Department
from subjects.models import Subject
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from .forms import DepartmentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class DashboardView(ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['teachers'] = Teacher.objects.all()
        ctx['groups'] = Group.objects.all()
        ctx['subjects'] = Subject.objects.all()
        ctx['groups_count'] = Group.objects.filter(status='ac').count()
        ctx['subject_names'] = list(Subject.objects.values_list('name', flat=True))
        ctx['subject_teachers_counts'] = [subject.teachers.count() for subject in Subject.objects.all()]
        return ctx


class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


class DepartmentsCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:depart_list')


class DepartmentsUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:depart_list')


class DepartmentsDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'departments'


class DepartmentsDeleteView(DeleteView):
    model = Department
    template_name = 'departments/list.html'
    success_url = reverse_lazy('departments:depart_list')


