from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(unique=True, max_length=300)
    published = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(unique=True, max_length=300)
    published = models.BooleanField()
    content = models.TextField()
    needs_IDE = models.BooleanField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LessonQuestion(models.Model):
    name = models.CharField(max_length=300)
    published = models.BooleanField()
    question = models.TextField()
    QUESTION_TYPE = (
        ('multiple_choice', 'multiple_choice'),
        ('fill_in_blank', 'fill_in_blank')
    )
    question_type = models.CharField(max_length=300, choices=QUESTION_TYPE)
    DIFFICULTY = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'lesson'], name='combination of lesson and name is unique')
        ]

class LessonQuestionOption(models.Model):
    option = models.CharField(max_length=500)
    option_correct = models.BooleanField()
    lesson_question = models.ForeignKey(LessonQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return self.option

class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'lesson'], name='combination of lesson and user is unique')
        ]