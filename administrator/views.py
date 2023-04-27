from django.shortcuts import render, redirect

from administrator.forms import TeacherRegisterForm
from authentication.models import user_type, User


# Create your views here.
def add_teachers(request):

    form = TeacherRegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            te = request.POST.get('teacher')
            user = User.objects.create_user(
                username=username,
            )

            user.set_password(password)
            user.save()

            usert = user_type(user=user, is_teacher=True)
            usert.save()
            form.send()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'add_teachers.html', context)

