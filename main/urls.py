from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics', views.topics, name='topics'),
    path('lessons/(<lesson_id>\d+)', views.lessons, name='lessons'),
    path('lesson_quizzes/(<lesson_id>\d+)', views.lesson_quizzes, name='lesson_quizzes'),
    path('validate/lesson_quiz', views.quiz_processing, name='quiz_processing')
]
