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
    print("SOMETHING!!!!!")
    template_name = 'registration/signup.html'


def home(request):
    print("ACà ESTAMOS")
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:notes_change_list')
        else:
            return redirect('students:notes_list')
    return render(request, 'school/home.html')


class Login(FormView):
    print("LOGIN!!!")
    template_name = 'registration/login.html'
    form_class = FormularioLogin
    print(form_class)
    success_url = reverse_lazy('school:teacher_list')




    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        print("ALGO ACA!!!")
        if request.user.is_authenticated:
            print("IFFFF", self.get_success_url())
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        print("FORM VALID LOGIN")
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def userLogout(request):
    print("LOGOUT", request)
    logout(request)
    return HttpResponseRedirect('/login/')
