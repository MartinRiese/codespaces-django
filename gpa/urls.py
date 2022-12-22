from django.urls import path

from . import views

urlpatterns = [
    path('course', views.CourseIndexView.as_view(), name='course_index'),
    path('student', views.StudentIndexView.as_view(), name='student_index'),
]
