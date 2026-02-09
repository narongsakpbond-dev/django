from rest_framework import serializers


from .models import Classroom, School, Student, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'short_name', 'address']


class SchoolDetailSerializer(SchoolSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + ['classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return obj.teachers.count()

    def get_student_count(self, obj):
        return obj.students.count()


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room']


class TeacherMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender']


class StudentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'gender']


class ClassroomDetailSerializer(ClassroomSerializer):
    teachers = TeacherMiniSerializer(many=True, read_only=True)
    students = StudentMiniSerializer(many=True, read_only=True)

    class Meta(ClassroomSerializer.Meta):
        fields = ClassroomSerializer.Meta.fields + ['teachers', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = ['id', 'school', 'firstname', 'lastname', 'gender', 'classrooms']


class ClassroomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room']


class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassroomMiniSerializer(many=True, read_only=True)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'school', 'classroom', 'firstname', 'lastname', 'gender']


class StudentDetailSerializer(StudentSerializer):
    classroom = ClassroomMiniSerializer(read_only=True)
