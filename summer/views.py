from django.shortcuts import render
from .models import Question

def index(request):
    elements = Question.objects.all()
    return render(request, 'index.html', {'elements': elements})
