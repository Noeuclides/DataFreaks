from django.views.generic import CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import TeacherSignUpForm, NoteForm
from ..models import CustomUser, Teacher, Course, Note



class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    print("VISTARETORNO: ", form_class)
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('school:student_list')


class ListCourseView(ListView):
    print("TEACHERLIST!!!")
    model = Teacher
    template_name = 'school/list_course.html'
    context_object_name = 'courses'

    def get_queryset(self):
        print(self.request.user.id, type(self.request.user.id))
        print(Course.objects.filter(teacher=self.request.user.id))
        return Course.objects.filter(teacher=self.request.user.id)


class StudentListView(ListView):
    model = Teacher
    template_name = 'school/student_list.html'
    context_object_name = 'students'
    success_url = reverse_lazy('school:students_list')

    def get_queryset(self):
        print(self.request.user, type(self.request.user.id))
        cor = Course.objects.filter(teacher=self.request.user.id)
        print(cor)
        print(Note.student)
        for student in Note.objects.filter(course=cor[0]):
            print(student.student)
        students = Note.objects.filter(course=cor[0])
        print(dir(students))
        print(students.all())
        return students.all()


class NoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'school/note_edit.html'
    success_url = reverse_lazy('school:student_note')


class NoteUpdateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'school/note_edit.html'
    success_url = reverse_lazy('school:student_note')