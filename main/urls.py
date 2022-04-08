from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('instructor',views.instructor, name='instructor'),
    path('topics', views.topics, name='topics'),
    path('add/topics', views.create_topic, name='create_topic'),
    path('edit/topic/(<topic_id>\d+)', views.edit_topic, name='edit_topic'),
    path('add/lessons', views.create_lesson, name='create_lesson'),
    path('edit/lesson/(<lesson_id>\d+)', views.edit_lesson, name='edit_lesson'),
    # path('add/questions', views.create_question, name='create'),
    path('lessons/(<lesson_id>\d+)', views.lessons, name='lessons'),
    path('lesson_quizzes/(<lesson_id>\d+)', views.lesson_quizzes, name='lesson_quizzes'),
    path('validate/lesson_quiz', views.quiz_processing, name='quiz_processing'),
    path('lesson/submit/comment', views.create_lesson_comment, name='create_lesson_comment'),
    path('lesson/delete/comment', views.delete_lesson_comment, name='delete_lesson_comment'),
    path('lesson/submit/comment/reply', views.create_lesson_comment_reply, name='create_lesson_comment_reply'),
    path('lesson/delete/comment/reply', views.delete_lesson_comment_reply, name='delete_lesson_comment_reply')
]
