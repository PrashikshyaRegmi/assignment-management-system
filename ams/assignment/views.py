from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import *
from .models import *


class Home(TemplateView):
    template_name = 'base.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def show(request):
    teachers = Teacher.objects.all()
    return render(request, 'show.html', {
        'teachers': teachers
    })


def tech(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = TeacherForm()
    return render(request, 'index.html', {
        'form': form
    })


def delete(request, pk):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
    return redirect('show')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'list.html'
    context_object_name = 'teacher'


class UploadTeacherView(CreateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('class_tech')
    template_name = 'index.html'

"""def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)"""


def show1(request):
    students = Student.objects.all()
    return render(request, 'show1.html', {
        'students': students
    })


def stud(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show1')
    else:
        form =StudentForm()
    return render(request, 'index1.html', {
        'form': form
    })


def delete1(request, pk):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
    return redirect('show')


class StudentListView(ListView):
    model = Teacher
    template_name = 'list1.html'
    context_object_name = 'student'


class UploadStudentView(CreateView):
    model =Student
    form_class = StudentForm
    success_url = reverse_lazy('class_stud')
    template_name = 'index.html'

