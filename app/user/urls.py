from django.urls import path, include, re_path
from user import views
from rest_framework.routers import DefaultRouter


app_name = 'user'

urlpatterns = [
    re_path('list/', views.UserListView.as_view(),name='list'),
    re_path('create/', views.UserCreateView.as_view(),name='create'),
]
