from rest_framework import viewsets

from testdb.models import Todo
from testdb.serializers.todo import testdbSerializer


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
