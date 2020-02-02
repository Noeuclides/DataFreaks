from django.views.generic import CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import TeacherSignUpForm
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
    success_url = reverse_lazy('school:students_list')