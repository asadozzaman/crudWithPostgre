from django.shortcuts import render
from first_app import forms
from first_app.models import Student
# Create your views here.
def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title': 'Index','student_list':student_list}
    return  render(request,'first_app/index.html',context=diction)

def student_form(request):
    form = forms.stduent_form

    if request.method =="POST":
        form = forms.stduent_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Student Form',"student_form": form}
    return  render(request,'first_app/student_form.html',context=diction)

def student_info(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    diction={'student_info':student_info}
    return render(request,'first_app/student_info.html',context=diction)

def student_update(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.stduent_form(instance=student_info)
    
    if request.method =="POST":
        form = forms.stduent_form(request.POST,instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'student_form':form}
    return render(request,'first_app/student_update.html',context=diction)        

def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction={'deletemessage': "Delete Done"}
    return render(request,'first_app/student_delete.html',context=diction)