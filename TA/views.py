from django.shortcuts import render
from django.http import HttpResponse

def index_page_view(request):
    return render(request, 'index.html')


def papers_page_view(request):
    return HttpResponse('papers')

def finishedpapers_page_view(request):
    return HttpResponse('finished papers')

def tostudent_page_view(request):
    return HttpResponse('tostudent')

def toadmin_page_view(request):
    return HttpResponse('toadmin')



