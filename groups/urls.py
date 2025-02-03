from django.urls import path
from . import views


app_name = 'groups'


urlpatterns = [
    path('list/', views.GroupListView.as_view(), name='groups_list'),
    path('create/', views.GroupCreateView.as_view(), name='create'),
    path('update/', views.GroupUpdateView.as_view(), name='update'),
    path('create/', views.GroupDetailView.as_view(), name='detail'),
    path('create/', views.GroupDeleteView.as_view(), name='delete'),
]