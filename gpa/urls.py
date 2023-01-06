from django.urls import path

from . import views


app_name = 'gpa'

urlpatterns = [
    path('course', views.CourseIndexView.as_view(), name='course_index'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:course_id>/update', views.update, name='course_update'),
    path('student', views.StudentIndexView.as_view(), name='student_index'),
]
