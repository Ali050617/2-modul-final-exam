from django.core.paginator import Paginator
from departments.models import Department
from .models import Subject
from django.urls import reverse_lazy
from .forms import SubjectForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'
    paginate_by = 10

    def get_queryset(self):
        subjects = Subject.objects.all()
        status = self.request.GET.get('status')
        department = self.request.GET.get('department')
        grade_level = self.request.GET.get('grade_level')
        search_query = self.request.GET.get('search')

        if status:
            subjects = subjects.filter(status=status)
        if department:
            subjects = subjects.filter(department=department)
        if grade_level:
            subjects = subjects.filter(grade_level=grade_level)
        if search_query:
            subjects = subjects.filter(name__icontains=search_query)

        return subjects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        subjects_page = paginator.get_page(page)

        context['subjects'] = subjects_page
        context['paginator'] = paginator
        context['departments'] = Department.objects.all()
        return context


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subject_list')

    def get_success_url(self):
        return reverse_lazy('subjects:subject_list')


class SubjectUpdatedView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects')


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subjects'


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/list.html'
    success_url = reverse_lazy('subjects_list')