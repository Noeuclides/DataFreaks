from django.urls import include, path
from django.contrib.auth.decorators import login_required

from .views import school, student, teacher

urlpatterns = [
    path('<int:pk>/', login_required(teacher.DetailCourseView.as_view()), name='students_list'),
    path('teacher/students/<int:pk>/', login_required(teacher.NoteView.as_view()), name='student_note'),
    path('teacher/', login_required(teacher.ListCourseView.as_view()), name='teacher_list'),

    #path('students/course/<int:pk>', login_required(student.StudentsCourseView.as_view()), name='students_course'),
    #path('student/', login_required(student.StudentSignUpView.as_view()), name='student_signup'),
    path('student/courses/', login_required(student.ListCourseView.as_view()), name='student_courses'),
]