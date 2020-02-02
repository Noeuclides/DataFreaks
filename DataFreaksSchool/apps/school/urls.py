from django.urls import include, path

from .views import school, student, teacher

urlpatterns = [
    path('teacher/students/', teacher.StudentListView.as_view(), name='students_list'),
    path('teacher/', teacher.ListCourseView.as_view(), name='teacher_list'),
    path('student/', student.StudentSignUpView.as_view(), name='student_signup'),
]