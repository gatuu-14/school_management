from django.contrib import admin
from .models import Student, Teacher, Fee, Timetable

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Fee)
admin.site.register(Timetable)
