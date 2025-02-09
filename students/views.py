from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student successfully created!")
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student successfully updated!")
        return super().form_valid(form)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/list.html'
    success_url = reverse_lazy('students:student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Student successfully deleted!")
        return super().delete(request, *args, **kwargs)
