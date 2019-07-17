from django.contrib import admin
from .models import Quiz , Question, QuizAttempt, Choice, QuestionAttempt
# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quizname','author')
admin.site.register(Quiz,QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questionname','quiz')
admin.site.register(Question,QuestionAdmin)

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('quiz','player','score')
admin.site.register(QuizAttempt,QuizAttemptAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice','is_correct')
admin.site.register(Choice,ChoiceAdmin)

class QuestionAttemptAdmin(admin.ModelAdmin):
    list_display = ('quizattempt','question','is_correct')
admin.site.register(QuestionAttempt,QuestionAttemptAdmin)

# from django.apps import apps
# # from django.contrib import admin

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass