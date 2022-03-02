from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics', views.topics, name='topics'),
    path('lesson_example', views.lesson_example, name='lesson_example'),
    path('lessons/(<lesson_id>\d+)', views.lessons, name='lessons'),
    path('lesson_quizzes/(<lesson_id>\d+)', views.lesson_quizzes, name='lesson_quizzes')
]
