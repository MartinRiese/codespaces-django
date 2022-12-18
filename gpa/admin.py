from django.contrib import admin

# Register your models here.
from .models import Course, Grade, Student

admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Student)