from django import forms
# from django.core import validators
from .models import Quiz,Question,Choice

class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ('quizname',)

# class QuestionForm(forms.ModelForm):

#     class Meta:
#         model = Question
#         fields = ('questionname',)

# class ChoiceForm(forms.ModelForm):
    
#     class Meta:
#         model = Choice
#         fields = ('choice','is_correct')

class QuestionAnswerForm(forms.Form):

    question = forms.CharField(max_length=350)
    option_1 = forms.CharField(max_length=40)
    is_option_1_correct = forms.BooleanField(required = False)
    option_2 = forms.CharField(max_length=40)
    is_option_2_correct = forms.BooleanField(required = False)
    option_3 = forms.CharField(max_length=40)
    is_option_3_correct = forms.BooleanField(required = False)
    option_4 = forms.CharField(max_length=40)
    is_option_4_correct = forms.BooleanField(required = False)

    def clean(self):
        cleaned_data = super(QuestionAnswerForm,self).clean()
        x=cleaned_data['is_option_1_correct'] or cleaned_data['is_option_2_correct'] or cleaned_data['is_option_3_correct'] or cleaned_data['is_option_4_correct']
        if not x:
            raise forms.ValidationError('atleat one correct answer is needed')
