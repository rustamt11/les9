from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
