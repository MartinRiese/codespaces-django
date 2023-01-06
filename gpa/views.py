from django.views import generic

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Course, Student


class CourseIndexView(generic.ListView):
    context_object_name = 'course_list'

    def get_queryset(self):
        """Return all courses"""
        return Course.objects.all()


class CourseDetailView(generic.DetailView):
    model = Course


# class CourseUpdateView(generic.UpdateView):
#     model = Course

def update(request, course_id):
    print(f"updating {course_id}: {request}")
    return HttpResponseRedirect(reverse('gpa:course_detail', args=(course_id,)))


class StudentIndexView(generic.ListView):
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return all students"""
        return Student.objects.all()
