from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you at the index")

def result(request, question_id):
    response = "you are looking at the result question %s"
