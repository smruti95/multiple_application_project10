from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def philips(request):
    return HttpResponse('good allrounder')
def conway(request):
    return HttpResponse('good opener')