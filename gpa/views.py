from django.views import generic

from .models import Course, Student


class CourseIndexView(generic.ListView):
    context_object_name = 'course_list'

    def get_queryset(self):
        """Return all courses"""
        return Course.objects.all()


class CourseDetailView(generic.DetailView):
    model = Course


class StudentIndexView(generic.ListView):
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return all students"""
        return Student.objects.all()
