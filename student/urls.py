from django.urls import path
from student import views

urlpatterns = [
    path('Host_student/', views.Host_student, name='Host_student'),
    path('view_quiz_student/', views.view_quiz_student, name='view_quiz_student'),
    path('view_quiz_details/', views.view_quiz_details, name='view_quiz_details'),
    path('view_quiz_score/', views.view_quiz_score, name='view_quiz_score'),
    path('view_next_question/', views.view_next_question, name='view_next_question'),

]
