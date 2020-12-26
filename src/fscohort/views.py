from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    my_context = {
        "title": "clarusway",
        "dict_1": {"djang": "best framework"},
        "my_list": [2, 3, 4, 5],
    }

    return render(request, "fscohort/home.html", my_context)

def about_view(request):
    return HttpResponse("Hi ,this is fscohort about page.")