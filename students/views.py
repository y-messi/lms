from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {'students': Student.objects.all()})

def view_student(request):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_locker_number = form.cleaned_data['locker_number']
            new_user_name = form.cleaned_data['user_name']
            new_phone_number = form.cleaned_data['phone_number']
            new_email = form.cleaned_data['email']
            new_enter_time = form.cleaned_data['enter_time']
            new_exit_time = form.cleaned_data['exit_time']
            
            new_student = Student(
                locker_number=new_locker_number,
                user_name=new_user_name,
                phone_number=new_phone_number,
                email=new_email,
                enter_time=new_enter_time,
                exit_time=new_exit_time
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
        'form': form
    })             
            
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))    
                    