from django.urls import path

from . import views

urlpatterns = [
    path('tasks/create/', views.create_task, name='task_create'),
    path('tasks/', views.tasks_list, name='tasks'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='task_delete'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
]

