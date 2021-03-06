from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Student, Course, CustomUser, Note, Teacher


class StudentSignUpForm(UserCreationForm):
    course = forms.ModelMultipleChoiceField(
        queryset = Course.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required= True
    )


    class Meta:
        model = CustomUser
        fields = ('full_name', 'username')
 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        cor = self.cleaned_data.get('course')
        print(cor[0])
        note = Note.objects.create(student=student, course=cor[0])
        print(note)
        student.courses.add(*self.cleaned_data.get('course'))
        print("hola", student)
        return user


class TeacherSignUpForm(UserCreationForm):
    course = forms.ModelMultipleChoiceField(
        queryset = Course.objects.filter(teacher__isnull=True),
        widget = forms.CheckboxSelectMultiple,
        required= True
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('full_name', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        courses = self.cleaned_data.get('course')
        print(courses)
        for course in courses:
            teacher.course_set.add(course)
        print(teacher.course_set.all())
        print('USER ', user)
        return user

class FormularioLogin(AuthenticationForm):
    print("FORMULOGIN!!")
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'password'


class NoteForm(forms.ModelForm):
    note = forms.FloatField( ) 
    class Meta:
        model = Note
        fields = ('note',)
        label = {
            'note':'Note'
        }
        widgets = {
            'titulo': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            )
        }