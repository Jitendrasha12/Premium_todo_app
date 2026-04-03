from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet
from .views import home_view

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Template views
    path('', home_view, name='home'),
]
