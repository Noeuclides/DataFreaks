from django.views.generic import CreateView, ListView, UpdateView
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
        print(self.request.user, type(self.request.user.id))
        course = Note.objects.filter(student=self.request.user.id)
        return course


class StudentsListView(ListView):
    model = Student
    template_name = 'school/students_course.html'
    context_object_name = 'students'
    success_url = reverse_lazy('school:students_course')


    def get_queryset(self):
        print(self.request.user, type(self.request.user.id))
        courses = Note.objects.filter(student=self.request.user.id)
        pi = Student.objects.prefetch_related('courses')
        print(courses)
        print(pi)
        for course in courses:
            print(course.course)
            print(course.student)

        return courses

