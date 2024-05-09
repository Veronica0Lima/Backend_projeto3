from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/users/', views.api_users),
    path('api/users/<int:user_id>/', views.api_user),
]