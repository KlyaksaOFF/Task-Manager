from django.urls import path

from . import views

urlpatterns = [
    path('statuses/', views.status, name='statuses'),
    path('statuses/create/', views.status_create, name='status_create'),
    path('statuses/<int:pk>/update/', views.update_status, name='status_update'),
    path('statuses/<int:pk>/delete/', views.delete_status, name='status_delete'),
]

