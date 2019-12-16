from django import forms

from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('teachername', 'teacheremail', 'teachersubject', 'assignments','duedate')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studentname', 'studentemail', 'subject','completiondate', 'studassignments','status')
