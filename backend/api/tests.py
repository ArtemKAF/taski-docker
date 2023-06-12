from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()
        return super().setUp()
    
    def test_list_exists(self):
        """Проверка доступности задач."""
        responce = self.guest_client.get('/api/tasks/')
        self.assertEqual(responce.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи."""
        data={'title': 'Test', 'description': 'Test'}
        responce = self.guest_client.post('/api/tasks/', data)
        self.assertEqual(responce.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())