from rest_framework import serializers

from .models import TodoTask


class TodoTaskSerialier(serializers.ModelSerializer):
    """TodoTask serializer"""

    class Meta:
        model = TodoTask
        fields = '__all__'
