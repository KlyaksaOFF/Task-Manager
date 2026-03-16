from django.contrib import admin
from django.urls import include, path

from task_manager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('users.urls')),
    path('', include('statuses.urls')),
    path('', include('labels.urls')),
    path('', include('tasks.urls')),
    path('admin', admin.site.urls),
    path('test-rollbar/', views.test_rollbar, name='test_rollbar'),
]
