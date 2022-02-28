from django.db import models

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