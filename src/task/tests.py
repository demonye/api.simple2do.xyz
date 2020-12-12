from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import factory

from .models import TodoTask


class TodoTaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoTask

    title = factory.Faker('text')


class TodoTaskTest(TestCase):
    """Test TodoTask API"""

    def setUp(self):
        self.client = APIClient()
        self.tasks = [
            TodoTaskFactory(),
            TodoTaskFactory(),
            TodoTaskFactory(),
        ]

    def test_get_task_list(self):
        resp = self.client.get(reverse('task_list_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)


