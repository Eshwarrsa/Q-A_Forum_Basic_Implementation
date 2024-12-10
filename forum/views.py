from django.shortcuts import render, get_object_or_404, redirect
from forum.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'question_list.html', {'questions' : questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk = pk)
    return render(request, 'question_detail.html', {"question" : question})

@login_required
def add_question(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Question.objects.create(title = title, description = description, author = request.user)
        return redirect('forum:question_list')
    return render(request, "add_question.html")

@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        Answer.objects.create(content = content, question = question, author = request.user)
        return redirect('forum:question_detail', pk = question.pk)
    return render(request, 'add_answer.html', {'question' : question})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})