
from django import forms

from django.contrib.auth import get_user_model

from django.core.mail import send_mail

from quiz import settings

User = get_user_model()


class TeacherRegisterForm(forms.ModelForm):
    # username = forms.CharField(max_length=20)
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    teacher = forms.BooleanField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'teacher'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("passwords must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used")
        return super(TeacherRegisterForm, self).clean(*args, **kwargs)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = self.clean()

        # name = cl_data.get('name').strip()
        to_email = cl_data.get('email')
        username = cl_data.get('username')
        password = cl_data.get('password')
        msg = 'Welcome to quizzard ' + 'Your login credentials as a teacher are'
        msg += f'\n"Username : {username} "\n\n'
        msg += f'\n"Password : {password} "\n\n'

        return msg, to_email

    def send(self):

        subject = "Login Credentials for quizzard"
        msg, to_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
