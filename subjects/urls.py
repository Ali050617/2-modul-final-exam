from django.urls import path
from . import views


app_name = 'subject'


urlpatterns = [
    path('list/', views.SubjectListView.as_view(), name='subject_list'),
    path('create/', views.SubjectCreateView.as_view(), name='create'),
    path('update/', views.SubjectUpdatedView.as_view(), name='update'),
    path('detail/', views.SubjectDetailView.as_view(), name='detail'),
    path('delete/', views.SubjectDeleteView.as_view(), name='delete'),
]