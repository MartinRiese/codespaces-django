from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    credit = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=200)


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.IntegerField()
