import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        try:
            logger.info("Retrieving all tasks")
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error retrieving tasks: {str(e)}")
            return Response({"error": "Failed to retrieve tasks"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            logger.info("Creating a new task")
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            logger.info(f"Updating task {kwargs.get('pk')}")
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error updating task: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            logger.info(f"Deleting task {kwargs.get('pk')}")
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error deleting task: {str(e)}")
            return Response({"error": "Failed to delete task"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
