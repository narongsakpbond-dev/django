
from rest_framework.viewsets import ModelViewSet

from ...models import School
from ...filters import SchoolFilter
from ...serializers import SchoolDetailSerializer, SchoolSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all().prefetch_related('classrooms', 'teachers', 'students')
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return super().get_serializer_class()
