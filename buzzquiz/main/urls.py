from django.conf.urls import url
from django.urls import path , include


from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('home',views.home,name='home'),
    path('create_quiz',views.create_quiz,name='create_quiz'),
    path('add_question/<int:quizid>',views.add_question,name='add_question'),
    path('play_quiz/<int:quiz_id>',views.play_quiz,name='play_quiz'),
]
