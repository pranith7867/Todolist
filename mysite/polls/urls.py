from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_index>/<str:pk>/', views.updateTask, name = "update_index"),
    path('delete>/<str:pk>/', views.deleteTask, name = "delete"),
    
]