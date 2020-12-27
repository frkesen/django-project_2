from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm



def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # return HttpResponse("Hi, this is fscohort Home page.")
    # form = StudentForm()
    # my_context = {
    #     "title": "clarusway",
    #     "dict_1": {"djang": "best framework"},
    #     "my_list": [2, 3, 4, 5],
    #     "form": form
    # }

    return render(request, "fscohort/home.html")

def student_list(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, "fscohort/student_add.html", context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, "fscohort/student_detail.html", context)

def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    return render(request, "fscohort/student_delete.html")

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "student": student,
        "form": form
    }
    return render(request, "fscohort/student_update.html", context)

# def about_view(request):
#     return HttpResponse("Hi ,this is fscohort about page.")