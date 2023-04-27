from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# @login_required
def home(request):
    # global flag
    # print(flag)
    # if flag==2:
    #     flag-=1
    #     print(flag)
    # print(flag)
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    print("Logout successful")
    return render(request, "home.html")


def student_home(request):
    return render(request, "student_home.html")


def super_user(request):
    return render(request, "admin_home.html")