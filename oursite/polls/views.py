from django.shortcuts import render

from polls.models import Question


def index(request):
    questions = Question.objects.all()

    context = {
        "questions": questions
    }
    return render(request, 'polls/index.html', context)
