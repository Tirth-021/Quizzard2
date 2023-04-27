
from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import authentication
from questions.models import Quiz_settings, Question, Options
from authentication.models import User, user_type


# Create your views here.
def Host_student(request):
    form = Quiz_settings.objects.filter(is_active=True)
    print(form)
    context = {'form': form}
    return render(request, 'quiz_view.html', context)


def view_quiz_student(request):
    gamepin = request.POST.get('gamepin')
    marks = 0
    print("game pin in view_quiz_student", gamepin)
    form = Quiz_settings.objects.filter(is_active=True, quiz_id=gamepin)[0]
    tpq = form.tpq
    ppq = form.ppq
    number_of_question = len(Question.objects.filter(quiz_id_id=gamepin))
    print("number of questions are ", number_of_question)
    question = Question.objects.filter(quiz_id_id=gamepin)[0]
    question_number = 0
    current_user = request.user
    username = current_user.username
    score = 0
    options = Options.objects.filter(que_id_id=question.id)
    context = {'form': form, 'tpq': tpq, 'ppq': ppq, 'question': question, 'options': options,
               'question_number': question_number, 'number_of_question': number_of_question, 'marks': marks,
               'score': score,'username':username}
    return render(request, 'attempt_quiz.html', context)


def view_quiz_details(request):
    gamepin = request.POST.get('gamepin')
    print(gamepin)
    marks = 0
    form = Quiz_settings.objects.filter(is_active=True, quiz_id=gamepin)[0]
    print(form)
    context = {'form': form, 'marks': marks}
    return render(request, 'view_quiz_details.html', context)


def view_next_question(request):
    question_number = int(request.POST.get('question_number'))
    gameid = request.POST.get('gameid')
    number_of_question = int(request.POST.get('number_of_question'))
    username = request.POST.get('username')
    marks = int(request.POST.get('marks'))
    print("Number of questions later is", number_of_question)
    print(gameid)
    print(number_of_question)

    # user = User.objects.filter(id=current_user)
    # username=user.username
    form = Quiz_settings.objects.filter(is_active=True, quiz_id=gameid)[0]
    print(form)
    score = int(request.POST.get('score'))
    tpq = form.tpq
    ppq = form.ppq
    points = int(form.ppq)

    print("Question number is ", question_number)
    question = Question.objects.filter(quiz_id_id=gameid)[question_number]
    options = Options.objects.filter(que_id_id=question.id)
    print("options are", options)
    answer = options.last()
    print("Answer is", answer.is_answer)

    response = request.POST.get('response')
    print("Response is", response)
    if response == answer.is_answer:
        score += 1
    marks = score * points
    print(f"Total marks at question number {question_number} is {marks}")
    question_number += 1

    if question_number < number_of_question:
        question = Question.objects.filter(quiz_id_id=gameid)[question_number]
        options = Options.objects.filter(que_id_id=question.id)
        context = {'form': form, 'gameid': gameid, 'marks': marks, 'score': score, 'tpq': tpq, 'ppq': ppq,
                   'question': question,'username':username,
                   'options': options, 'question_number': question_number, 'number_of_question': number_of_question}

        current_user = request.user
        username = current_user.username
        print(username)
        channel_layer = get_channel_layer()
        channel_layer.group_send(
            'leaderboard',
            {
                'type': 'leaderboard.update',
                'user_name': username,
                'score': score,
                'question': question,
            }
        )



        return render(request, 'attempt_quiz.html', context)
    else:
        context = {'marks': marks}
        return render(request, 'view_score.html', context)


def view_quiz_score(request):
    print("Now in view_quiz_score")
    marks = request.POST.get('marks')

    gamepin = request.POST.get('gameid')
    # print("Game pin in view_quiz_score", gamepin)
    # score = 0
    # form = Quiz_settings.objects.filter(quiz_id=gamepin)[0]
    # print(form.quiz_name)
    # points = int(form.ppq)
    # print(points)
    # question = Question.objects.filter(quiz_id_id=gamepin)[0]
    # print(question)
    # options = Options.objects.filter(que_id_id=question.id)
    # print(options)
    # # answer = Options.objects.filter(options.is_answer)[0]
    # answer = options.last()
    # print(answer.is_answer)
    # response = request.POST.get('response')
    # if response == answer.is_answer:
    #     score += 1
    # marks = score * points
    # print("Total marks are", marks)
    context = {'marks': marks, 'gamepin': gamepin}
    return render(request, 'view_score.html', context)


def get_leaderboard_data(marks, username):
    return marks, username


def update_leaderboard():
    channel_layer = get_channel_layer()
    leaderboard = get_leaderboard_data()
    async_to_sync(channel_layer.group_send)(
        "leaderboard",
        {
            "type": "leaderboard_update",
            "leaderboard": leaderboard
        }
    )
