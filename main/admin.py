from django.contrib import admin
from .models import Topic, Lesson, LessonQuestion, LessonQuestionOption, UserLessonProgress

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(LessonQuestion)
admin.site.register(LessonQuestionOption)
admin.site.register(UserLessonProgress)