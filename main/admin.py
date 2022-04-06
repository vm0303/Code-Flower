from django.contrib import admin
from .models import *

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(LessonQuestion)
admin.site.register(LessonQuestionOption)
admin.site.register(UserLessonProgress)
admin.site.register(LessonParagraph)
admin.site.register(LessonComment)