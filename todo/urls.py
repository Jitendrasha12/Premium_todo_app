from django.urls import path
from .api_views import TaskListCreateAPIView, TaskDetailAPIView
from .views import home_view

urlpatterns = [
    # API endpoints (Raw SQL Implementation)
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    
    # Template views
    path('', home_view, name='home'),
]
