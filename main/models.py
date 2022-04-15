from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q

class Topic(models.Model):
    name = models.CharField(unique=True, max_length=300)
    published = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    min_passing_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(min_passing_score__gte=0.0) & Q(min_passing_score__lte=100.0),
                name='topic_min_passing_score_range'
            )
        ]

class Lesson(models.Model):
    name = models.CharField(unique=True, max_length=300)
    published = models.BooleanField()
    content_description = models.TextField()
    needs_IDE = models.BooleanField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    wanted_number_quiz_questions = models.PositiveSmallIntegerField()
    min_passing_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(min_passing_score__gte=0.0) & Q(min_passing_score__lte=100.0),
                name='lesson_min_passing_score_range',
            )
        ]

class LessonParagraph(models.Model):
    paragraph = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.paragraph

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
    option = models.TextField()
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

class LessonComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson.name

class LessonCommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(LessonComment, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent.body


class InstructorRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True,)
    email = models.CharField(max_length=300)
    reason = models.TextField()
    STATS = (
        ("pending", 'pending'),
        ("denied", "denied"),
        ("accepted", "accepted")
    )
    status = models.CharField(max_length=20, choices=STATS)

    def __str__(self):
        return self.email