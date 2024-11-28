from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def siri(request):
    return HttpResponse('<h1><marquee>my name is siri i like dancing</h1></marquee>')
