from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('we are connected !!')


def About(request):
    return HttpResponse('we are in about page..')

