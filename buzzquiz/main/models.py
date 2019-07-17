from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Quiz(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    quizname = models.CharField(max_length=30)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.quizname

class Question(models.Model):
    questionname = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)

    def __str__(self):
        return self.questionname

class Choice(models.Model):
    choice = models.CharField(max_length=30)
    is_correct=models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.choice

class QuizAttempt(models.Model):
    attempted_on = models.DateTimeField(default = timezone.now)
    score = models.IntegerField(default=0)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)

class QuestionAttempt(models.Model):
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    quizattempt = models.ForeignKey(QuizAttempt, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

# class Score(models.Model):
#     score = models.IntegerField(default=0)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     quizattempt = models.ForeignKey(QuizAttempt, on_delete = models.CASCADE)