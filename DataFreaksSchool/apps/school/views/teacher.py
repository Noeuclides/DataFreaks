from django.views.generic import CreateView, ListView, UpdateView, DetailView
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
        return redirect('school:teacher_list')


class ListCourseView(ListView):
    model = Course
    template_name = 'school/list_course.html'
    context_object_name = 'courses'

    def get_queryset(self):
        print(self.request.user.id, type(self.request.user.id))
        print(Course.objects.filter(teacher=self.request.user.id))
        return Course.objects.filter(teacher=self.request.user.id)


class DetailCourseView(DetailView):
    model = Course
    template_name = 'school/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        print(self.request.user.id, type(self.request.user.id))
        print(Course.objects.filter(teacher=self.request.user.id))
        return Course.objects.filter(teacher=self.request.user.id)

class NoteView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'school/note_edit.html'
    success_url = reverse_lazy('school:student_note')


# class NoteUpdateView(CreateView):
#     model = Note
#     form_class = NoteForm
#     template_name = 'school/note_edit.html'
#     success_url = reverse_lazy('school:student_note')