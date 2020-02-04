from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from ..forms import FormularioLogin
from ..models import CustomUser


class SignUpView(TemplateView):
    model = CustomUser
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:notes_change_list')
        else:
            return redirect('students:notes_list')
    return render(request, 'school/home.html')


class Login(FormView):
    template_name = 'registration/login.html'
    form_class = FormularioLogin


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        user = form.get_user()
        login(self.request,user)
        return super(Login,self).form_valid(form)

    def get_success_url(self):
        if self.request.user.is_teacher:
            return reverse_lazy('school:teacher_list')
        else:
            return reverse_lazy('school:student_courses')


def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
