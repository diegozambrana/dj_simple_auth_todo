from rest_framework import viewsets
from rest_framework.response import Response
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        queryset, created = Todo.objects.get_or_create(user=request.user);
        serializer = TodoSerializer(queryset)

        return Response(serializer.data)

    def update(self, request):
        try:
            queryset, created = Todo.objects.get_or_create(user=request.user);
            queryset.todo_json = request.data['json_data']
            queryset.save()
            return Response({'message': 'success'}, status=201)
        except:
            return Response({'message': 'Error'}, status=400)
