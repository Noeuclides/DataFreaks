from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from ..models import CustomUser



class SignUpView(TemplateView):
    model = CustomUser
    print("SOMETHING!!!!!")
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:notes_change_list')
        else:
            return redirect('students:notes_list')
    return render(request, 'school/home.html')