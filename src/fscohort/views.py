from django.shortcuts import render
from django.http import HttpResponse

from fscohort.forms import StudentForm


def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # return HttpResponse("Hi, this is fscohort Home page.")
    form = StudentForm()
    my_context = {
        "title": "clarusway",
        "dict_1": {"djang": "best framework"},
        "my_list": [2, 3, 4, 5],
        "form": form
    }

    return render(request, "fscohort/home.html", my_context)

def about_view(request):
    return HttpResponse("Hi ,this is fscohort about page.")