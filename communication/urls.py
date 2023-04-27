from django.urls import path
from communication import views
urlpatterns = [
    path('Host',views.Host,name='Host'),
    path('external',views.external,name='external'),
    path('view_quiz',views.view_quiz,name='view_quiz'),
    path('publish',views.publish,name='publish'),
    path('publish/<int:quiz_id>/',views.publish,name='publish'),
    path('publish_quiz/',views.publish_quiz,name='publish_quiz'),
]
