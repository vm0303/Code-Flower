from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics', views.topics, name='topics'),
    path('lesson_example', views.lesson_example, name='lesson_example')
]
