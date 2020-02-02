from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    full_name = models.CharField(max_length=50)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.full_name


class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL ,blank=True, null=True)


    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField(Course, through='Note', related_name='students', blank=True)

    def __str__(self):
        return self.user.full_name


class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='notes')
    note = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)], blank=True, null=True)

    def __str__(self):
        return str(self.note)