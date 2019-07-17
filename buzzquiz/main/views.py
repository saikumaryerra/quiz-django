from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
@login_required
def home(request):
    quizzes = Quiz.objects.all()
    leaderboard = QuizAttempt.objects.all().order_by('score')
    return render(request,'home.html',{'leaderboard' : leaderboard,'quizzes':quizzes})
@login_required
def profile(request):
    my_quizzes = Quiz.objects.filter(author = request.user)
    my_quiz_attempts = QuizAttempt.objects.filter(player = request.user).order_by('id')
    return render(request,'profile.html',{'my_quizzes' : my_quizzes,'my_quiz_attempts' : my_quiz_attempts})

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            # add_question(request,quiz.id)

            return redirect('add_question',quizid = quiz.id)
    else:
        form = QuizForm()
    return render(request,'create_quiz.html',{'form' : form})

@login_required
def add_question(request,quizid):
    if request.method == 'POST':
        question_form = QuestionAnswerForm(request.POST)
        
        if question_form.is_valid():
            form_data = question_form.cleaned_data
            question = Question.objects.create(quiz = Quiz.objects.get(pk=quizid) )
            question.questionname=form_data['question']
            
            option_1 = Choice.objects.create(question = Question.objects.get(pk = question.id) )
            option_1.choice = form_data['option_1']
            option_1.is_correct = form_data['is_option_1_correct']
            
            option_2 = Choice.objects.create(question = Question.objects.get(pk = question.id) )
            option_2.choice = form_data['option_2']
            option_2.is_correct = form_data['is_option_2_correct']

            option_3 = Choice.objects.create(question = Question.objects.get(pk = question.id) )
            option_3.choice = form_data['option_3']
            option_3.is_correct = form_data['is_option_3_correct']

            option_4 = Choice.objects.create(question = Question.objects.get(pk = question.id) )
            option_4.choice = form_data['option_4']
            option_4.is_correct = form_data['is_option_4_correct']

            question.save() 
            option_1.save()
            option_2.save()
            option_3.save()
            option_4.save()
            return redirect('add_question',quizid=quizid)
    else:
        question_form = QuestionAnswerForm()
    return render(request,'add_question.html',{'question_form': question_form , 'quizid':quizid})

@login_required
def play_quiz(request,quiz_id):
    pass