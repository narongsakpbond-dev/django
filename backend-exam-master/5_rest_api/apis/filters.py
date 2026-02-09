from django_filters import FilterSet, filters


from .models import Classroom, School, Student, Teacher


class SchoolFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(FilterSet):
    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(FilterSet):
    firstname = filters.CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='lastname', lookup_expr='icontains')
    classroom = filters.NumberFilter(field_name='classrooms', lookup_expr='exact')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']


class StudentFilter(FilterSet):
    firstname = filters.CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='lastname', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']
