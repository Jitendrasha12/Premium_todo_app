from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class TaskListCreateAPIView(APIView):
    """
    Handles listing todos and creating a new todo using raw SQL.
    """
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, description, due_date, status, created_at, updated_at FROM todo_task ORDER BY created_at DESC")
                columns = [col[0] for col in cursor.description]
                tasks = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            return Response(tasks)
        except Exception as e:
            logger.error(f"Error fetching tasks: {str(e)}")
            return Response({"error": "Failed to retrieve tasks"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description', '')
        due_date = data.get('due_date')
        status_val = data.get('status', 'Pending')
        created_at = timezone.now()
        updated_at = timezone.now()

        if not title or not due_date:
            return Response({"error": "Title and due_date are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO todo_task (title, description, due_date, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                    [title, description, due_date, status_val, created_at, updated_at]
                )
                new_id = cursor.fetchone()[0]
            
            return Response({
                "id": new_id,
                "title": title,
                "description": description,
                "due_date": due_date,
                "status": status_val,
                "created_at": created_at,
                "updated_at": updated_at
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):
    """
    Handles retrieving, updating, and deleting a specific todo using raw SQL.
    """
    def get(self, request, pk):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, description, due_date, status, created_at, updated_at FROM todo_task WHERE id = %s", [pk])
                row = cursor.fetchone()
                if not row:
                    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
                
                columns = [col[0] for col in cursor.description]
                task = dict(zip(columns, row))
            return Response(task)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        data = request.data
        title = data.get('title')
        description = data.get('description', '')
        due_date = data.get('due_date')
        status_val = data.get('status', 'Pending')
        updated_at = timezone.now()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE todo_task SET title=%s, description=%s, due_date=%s, status=%s, updated_at=%s WHERE id=%s",
                    [title, description, due_date, status_val, updated_at, pk]
                )
                if cursor.rowcount == 0:
                    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({"message": "Task updated successfully"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Simplified patch using raw SQL by checking which fields are provided
        data = request.data
        updated_at = timezone.now()
        
        # Build SQL dynamically for partially updated fields
        allowed_fields = ['title', 'description', 'due_date', 'status']
        update_fields = []
        params = []
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field}=%s")
                params.append(data[field])
        
        if not update_fields:
            return Response({"message": "No fields provided for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        update_fields.append("updated_at=%s")
        params.append(updated_at)
        params.append(pk)
        
        sql = f"UPDATE todo_task SET {', '.join(update_fields)} WHERE id=%s"
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, params)
                if cursor.rowcount == 0:
                    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"message": "Task partially updated"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM todo_task WHERE id = %s", [pk])
                if cursor.rowcount == 0:
                    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
