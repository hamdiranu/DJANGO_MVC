from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    question = Question.object.get()
    return render(request, 'hospital/index.html', {
        'question':"ini question",
       }   
       )


def detail(request, quest_id):
    question = Question.object.get(pk = quest_id)
    choice = Choice.object.filter(question = question_id).all()
    ctx = {
        'question': question,
        'choice' : choice
    }

    return render(request, 'polls/detail.html',ctx)

