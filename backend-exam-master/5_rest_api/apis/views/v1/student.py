
from rest_framework.viewsets import ModelViewSet

from ...models import Student
from ...filters import StudentFilter
from ...serializers import StudentDetailSerializer, StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().select_related('classroom')
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return super().get_serializer_class()
