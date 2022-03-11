from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Lesson
from django.http import JsonResponse

def home(request):
    return render(request, 'main/home.html')

def topics(request):
    all_topics = Topic.objects.all()
    context = {'topics': all_topics}
    return render(request, 'main/topics.html', context)

def lessons(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'main/lessons.html', context)

def lesson_quizzes(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'main/lesson_quizzes.html', context)

def quiz_processing(request):
    return JsonResponse({'love': 'is not defined'})