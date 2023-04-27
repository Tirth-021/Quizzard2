from django.urls import path
from administrator import views

urlpatterns =[
    path('add_teachers/', views.add_teachers, name='add_teachers')
]