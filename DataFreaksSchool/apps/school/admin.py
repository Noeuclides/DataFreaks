from django.contrib import admin
from .models import CustomUser, Student, Teacher, Course, Note

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Note)