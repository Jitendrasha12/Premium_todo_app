import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task
from django.utils import timezone

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_task(db):
    return Task.objects.create(
        title="Test Task",
        description="Test Desc",
        due_date=timezone.now(),
        status="Pending"
    )

@pytest.mark.django_db
def test_create_task(api_client):
    url = reverse('task-list')
    data = {
        "title": "New Task",
        "description": "New Description",
        "due_date": timezone.now().isoformat(),
        "status": "Pending"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    assert Task.objects.get().title == "New Task"

@pytest.mark.django_db
def test_retrieve_tasks(api_client, sample_task):
    url = reverse('task-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == sample_task.title

@pytest.mark.django_db
def test_full_update_task(api_client, sample_task):
    url = reverse('task-detail', kwargs={'pk': sample_task.id})
    data = {
        "title": "Updated Title",
        "description": "Updated Description",
        "due_date": timezone.now().isoformat(),
        "status": "Completed"
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    sample_task.refresh_from_db()
    assert sample_task.title == "Updated Title"
    assert sample_task.status == "Completed"

@pytest.mark.django_db
def test_delete_task(api_client, sample_task):
    url = reverse('task-detail', kwargs={'pk': sample_task.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0
