from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world, welcome to polls app!')


def detail(request, question_id):
    return HttpResponse(f'you are looking for question {question_id}')


def result(request, question_id):
    return HttpResponse(f'you are looking for result question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'you are voting for question {question_id}')