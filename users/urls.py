from django.urls import path

from . import views

urlpatterns = [
    path('users/create/', views.registration_user, name='registration_user'),
    path('login/', views.login_user, name='login'),
    path('users/', views.users, name='users'),
    path('logout/', views.logout, name='logout'),
    path('users/<int:pk>/update/', views.update_user, name='update'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete'),
]

