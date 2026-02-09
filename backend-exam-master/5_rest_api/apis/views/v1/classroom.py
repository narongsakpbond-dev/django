from rest_framework.viewsets import ModelViewSet

from ...models import Classroom
from ...filters import ClassroomFilter
from ...serializers import ClassroomDetailSerializer, ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all().prefetch_related('teachers', 'students')
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return super().get_serializer_class()
