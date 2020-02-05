from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import StudentSignUpForm
from ..models import CustomUser, Student, Course, Note


class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('school:student_courses')


class ListCourseView(ListView):
    model = Student
    template_name = 'school/student_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        print(self.request.user)
        my_notes = Note.objects.filter(student=self.request.user.id)      
        all_notes = Note.objects.all()
        courses = {}
        for note in all_notes:
            for mynote in my_notes:
                if note.course == mynote.course:
                    if mynote.course in courses.keys():
                        student = note.student
                        courses[mynote.course][1].append(student)
                    else:
                        students, course = [], []
                        students.append(note.student)
                        course = [note, students]
                        courses[mynote.course] = course
        courses['student'] = self.request.user
        print(courses)
        return courses
