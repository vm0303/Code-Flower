from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Lesson, LessonQuestion, LessonQuestionOption, UserLessonProgress
from django.http import JsonResponse
import json, math

def home(request):
    return render(request, 'main/home.html')

def achievements(request):
    return render(request, 'main/achievements.html')

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
    quiz = request.POST['quiz']
    quiz = json.loads(quiz)
    total_points = 0
    number_questions = 0
    lesson_obj = None

    for question in quiz:
        number_questions += 1

        for question_id, answers in question.items():
            question_obj = LessonQuestion.objects.get(id=question_id)
            correct_options = LessonQuestionOption.objects.filter(option_correct=True, lesson_question=question_obj)
            number_correct_options = len(correct_options)
            number_options_answered_correct = 0

            if not lesson_obj:
                lesson_obj = question_obj.lesson

            for answer in answers:
                for opt_id, option_choice in answer.items():
                    option_obj = LessonQuestionOption.objects.get(id=opt_id)

                    if option_obj.option_correct:
                        if isinstance(option_choice, str):
                            if option_choice == option_obj.option.strip():
                                number_options_answered_correct += 1
                        else:
                            number_options_answered_correct += 1

                    total_points +=  number_options_answered_correct / number_correct_options

    score = (total_points / number_questions) * 100
    score = math.trunc(score)
    best_score = score
    try:
        user_progress = UserLessonProgress.objects.get(user=request.user, lesson=lesson_obj)
        best_score = user_progress.score

        if user_progress.score <= score:
            best_score = score
            user_progress.score = score
            user_progress.save()
    except UserLessonProgress.DoesNotExist:
        user_progress = UserLessonProgress(user=request.user, lesson=lesson_obj, score=score)
        user_progress.save()

    return JsonResponse({'score': score, 'best-score': best_score})