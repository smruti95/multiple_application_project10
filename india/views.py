from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse(' run machine')
def rohit(request):
    return HttpResponse('hit man')