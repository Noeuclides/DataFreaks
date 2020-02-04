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
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('school:teacher_list')


class ListCourseView(ListView):
    model = Note
    template_name = 'school/list_course.html'
    context_object_name = 'courses'

    def get_queryset(self):
        print(self.request.user.id, type(self.request.user.id))        
        courses = Course.objects.filter(teacher=self.request.user.id)            
        return courses


class DetailCourseView(DetailView):
    model = Note
    template_name = 'school/student_list.html'
    context_object_name = 'students'

    def get_object(self, **kwargs):
        obj = self.kwargs['pk']
        print(obj)
        note = Note.objects.filter(course=obj)
        student = []
        for n in note:
            student.append(n)
            print(n.student, n.course)
        return student


class NoteView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'school/note_edit.html'

    def get_success_url(self):
        print(self.object.course)
        return reverse_lazy('school:students_list', kwargs={'pk' : self.object.course.pk})


