from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Lesson, LessonQuestion, LessonQuestionOption, UserLessonProgress

from django.http import JsonResponse
import json, math

def home(request):
    return render(request, 'main/home.html')

def topics(request):
    if not request.user.is_authenticated:
        return render(request, 'main/home.html', {'no_auth_message': True})

    all_topics = Topic.objects.all()
    context = {'topics': all_topics}
    return render(request, 'main/topics.html', context)

def lessons(request, lesson_id):
    if not request.user.is_authenticated:
        return render(request, 'main/home.html', {'no_auth_message': True})

    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'main/lessons.html', context)

def lesson_quizzes(request, lesson_id):
    if not request.user.is_authenticated:
        return render(request, 'main/home.html', {'no_auth_message': True})

    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'main/lesson_quizzes.html', context)

def instructor(request):
    if request.user.is_superuser:
        all_topics = Topic.objects.all()
        context = {'topics': all_topics}
        return render(request, 'main/admin.html', context)
    else:
        return render(request, 'main/home.html')

def create_topic(request):
    if not request.user.is_superuser:
        return render(request, 'main/home.html')

    if request.method == 'POST':
        topic = request.POST.get('topic')
        published = request.POST.get('published')
        score = request.POST.get('min_passing_score')

        new_topic = Topic(name=topic, published=published, min_passing_score=score)
        new_topic.save()
    # return JsonResponse({'topic': topic})
    # return HttpResponseRedirect('main/topics.html')
    return render(request, 'main/home.html')

def edit_topic(request, topic_id):
    if not request.user.is_superuser:
        return render(request, 'main/home.html')

    topic = Topic.objects.get(id=topic_id)
    lesson = Lesson.objects.filter(topic = topic_id)


    context = {'topics': topic, 'lessons': lesson}
    return render(request, 'main/add_lesson.html', context)

def create_lesson(request):
    if not request.user.is_superuser:
        return render(request, 'main/home.html')

    if request.method == 'POST':
        lname = request.POST.get('lname')
        desc = request.POST.get('desc')
        minScore = request.POST.get('min_score')
        quizNum = request.POST.get('quiz_num')
        published = request.POST.get('published')
        ide = request.POST.get('ide')
        topic_id = request.POST.get('topic')
        topic = Topic.objects.get(id=topic_id)

        new_lesson = Lesson(name=lname, published=published, content_description=desc, needs_IDE=ide, topic=topic,
                            wanted_number_quiz_questions=quizNum, min_passing_score=minScore)
        new_lesson.save()

    return JsonResponse({})

def edit_lesson(request, lesson_id):
    if not request.user.is_superuser:
        return render(request, 'main/home.html')

    lesson = Lesson.objects.get(id=lesson_id)
    quiz = LessonQuestion.objects.filter(lesson = lesson_id)

    context = {'lesson': lesson, 'quiz': quiz}
    return render(request, 'main/add_quizzes.html', context)

def quiz_processing(request):
    if not request.user.is_authenticated:
        return render(request, 'main/home.html', {'no_auth_message': True})

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