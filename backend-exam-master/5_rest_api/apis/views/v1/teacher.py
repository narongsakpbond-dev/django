
from rest_framework.viewsets import ModelViewSet

from ...models import Teacher
from ...filters import TeacherFilter
from ...serializers import TeacherDetailSerializer, TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all().prefetch_related('classrooms')
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return super().get_serializer_class()
