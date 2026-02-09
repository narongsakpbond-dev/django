from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self) -> str:
        return self.short_name or self.name


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.PositiveIntegerField()
    room = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['school', 'grade', 'room'], name='uniq_classroom_per_school')
        ]

    def __str__(self) -> str:
        return f"{self.school.short_name or self.school.name} {self.grade}/{self.room}"


class Teacher(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=Gender.choices)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
