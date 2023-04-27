from django.contrib import messages
from django.shortcuts import render, redirect
import sys
# from communication import server
from .server import socket_create
import socket
import random
from questions.models import Quiz_settings, Question, Options


# from .server import server1

# Create your views here.
def Host(request):
    return render(request, "Host.html")


# def getUsers(*userLise):
#     return userList = *userLise


x = []


def external(request):
    s = socket_create()
    y = s.main()
    s.listing_connections()
    # context={
    #     'external':y
    # }
    # s.listing_connections()
    # getUsers()
    # context = {
    #     'external': y
    # }
    # out=run([sys.executable,'//Users//tarun.advani//Documents//quizzard//communication//server.py'],shell=False,stdout=PIPE)
    # print(out)

    return render(request, "publish.html")


# def view_quiz(request,pk):
#     quiz = Quiz_settings.objects.get(pk=pk)
#     return render(request, 'publish/quiz.html', {'obj': quiz})

def view_quiz(request):
    current_user = request.user.id
    form = Quiz_settings.objects.filter(user_id_id=current_user)
    context = {'form': form}
    return render(request, 'quizlist.html', context)


def publish(request):
    quiz_id = request.GET.get('quiz_id')
    print(quiz_id)
    # context = {'id': quiz_id}

    quiz = Quiz_settings.objects.filter(quiz_id=quiz_id)
    print(quiz[0].quiz_name)
    print(quiz[0].description)
    context = {'quiz': quiz[0]}
    return render(request, 'publish.html', context)


def publish_quiz(request):
    quiz_id = request.GET.get('quiz_id')
    print(quiz_id)
    quiz = Quiz_settings.objects.filter(quiz_id=quiz_id)
    print(quiz)
    # quiz[0].is_active = True
    quiz.update(is_active=True)
    print(quiz[0].is_active)
    messages.success(request, "Your quiz is published successfully.")
    return render(request, 'index.html')
