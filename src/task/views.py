from django.shortcuts import render
from rest_framework import mixins, viewsets, exceptions

from .serializers import TodoTaskSerialier
from .models import TodoTask


class TodoTaskView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """TaskAPIView. """

    queryset = TodoTask.objects.filter(is_archived=False)
    serializer_class = TodoTaskSerialier

    def destroy(self, request, pk):
        if self.get_object().is_archived:
            raise exceptions.NotFound
        return super().destroy(request, pk)
