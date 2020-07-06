from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('task/add/', views.task_add, name='task_add'),
    #path('update/<int:pk>',views.task_update),
    path('delete/<int:pk>', views.task_delete),
]