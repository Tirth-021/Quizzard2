
from django.shortcuts import render, redirect
from authentication.models import user_type, User
import jwt

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)

from .forms import UserRegisterForm, UserLoginform



def login_view(request):
    # next = request.GET.get('next')
    # print(next)
    form = UserLoginform(request.POST or None)
    # if form.is_valid():
    #
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
    #     # te = request.POST.get('teacher')
    #
    #     # encoded_token = jwt.encode({'name': username, 'passw': password}, 'tsa', algorithm='HS256')
    #     # print(encoded_token)
    #
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         type_obj = user_type.objects.get(user=user)
    #         if user.is_authenticated and type_obj.is_teach:
    #             return redirect('index')
    #         else:
    #             return redirect('index2')
    #
    #     # if next:
    #     #     return redirect(next)
    #     # if te:
    #     #     return redirect("/index/")
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'login.html', context)
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect('signup')
        login(request, user)
        type_obj = user_type.objects.filter(user=user)
        print(type_obj)
        if user.is_superuser:
            print("Super user detected")
            return redirect('/super')
        if user.is_authenticated and type_obj[0].is_teacher:
            print("Teacher detected")
            return redirect('/index')
        else:
            print("Student detected")
            return redirect('/shome')

    context = {
        'form': form,
     }
    return render(request, 'login.html', context)


def register_view(request):
    # next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     password = form.cleaned_data.get('password')
    #     user.set_password(password)
    #     te = request.POST.get('teacher')
    #     user = User.objects.create_user(
    #         username=user,
    #     )
    #     user.set_password(password)
    #     user.save()
    #     new_user = authenticate(username=user.username, password=password)
    #     if te:
    #         usert = user_type(user=user, is_author=True)
    #     else:
    #         usert = user_type(user=user, is_teach=False)
    #     usert.save()
    #     # login(request, new_user)
    #     if next:
    #         return redirect(next)
    #     return redirect('login')
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, "signup.html", context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
        )

        user.set_password(password)
        user.save()

        usert = user_type(user=user, is_student=True)
        # if te:
        #     usert = user_type(user=user, is_student=True)
        # elif st:
        #     usert = user_type(user=user, is_teacher=True)
        # else:
        #     usert = user_type(user=user, is_administrator=True)
        usert.save()
        return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


