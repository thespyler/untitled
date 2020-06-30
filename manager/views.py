from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
def home_page(request):
	return render(request, 'home.html',
				{'questions': Question.objects.all(),
				 'users': Users.objects.all()
				}
				)
# Create your views here.
def ask(request):
	return render(request, 'question.html')

def save(request):
	question = request.POST['question']

def qna(request, id):
	q = Question.objects.get(id=id)
	return render(request, 'next.html', {'obj': q})

	q_to_ask = Question(question=question)
	q_to_ask.save()
	return HttpResponseRedirect('/')

def signin(request):
	return render(request, 'signin.html')

def save_name(request):
	nm = request.POST['nm']
	a = Users(name=nm)
	a.save()
	return HttpResponseRedirect('/')