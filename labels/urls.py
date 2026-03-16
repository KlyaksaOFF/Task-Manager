from django.urls import path

from . import views

urlpatterns = [
    path('labels/', views.label, name='labels'),
    path('labels/create/', views.create_label, name='create_label'),
    path('labels/<int:pk>/update/', views.update_label, name='label_update'),
    path('labels/<int:pk>/delete/', views.delete_label, name='label_delete'),
]

