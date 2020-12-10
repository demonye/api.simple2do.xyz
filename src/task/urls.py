from django.urls import path
from .views import TodoTaskView


methods_map = {
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
}


def methods(*args):
    return {m: methods_map[m] for m in args if m in methods_map}


urlpatterns = [
    path('', TodoTaskView.as_view(methods('get', 'post')), name='task_list_create'),
    path('<int:pk>/', TodoTaskView.as_view(methods('patch', 'delete')), name='task_update_delete'),
]
