from django.contrib import admin
from .models import *

admin.site.site_title = "CodeFlower"
admin.site.site_header = "CodeFlower"
admin.site.index_title = "CodeFlower"

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(LessonQuestion)
admin.site.register(LessonQuestionOption)
admin.site.register(UserLessonProgress)
admin.site.register(LessonParagraph)
admin.site.register(LessonComment)
admin.site.register(LessonCommentReply)
admin.site.register(InstructorRequest)