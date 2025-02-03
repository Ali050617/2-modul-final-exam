from django.urls import path
from . import views


app_name = 'student'


urlpatterns = [
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('create/', views.StudentCreateView.as_view(), name='create'),
    path('update/', views.StudentUpdatedView.as_view(), name='update'),
    path('detail/', views.StudentDetailView.as_view(), name='detail'),
    path('delete/', views.StudentDeleteView.as_view(), name='delete'),
]