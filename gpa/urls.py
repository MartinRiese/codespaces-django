from django.urls import path

from . import views

urlpatterns = [
    path('course', views.IndexView.as_view(), name='course_index'),
]
