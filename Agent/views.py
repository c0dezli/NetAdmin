from django.shortcuts import render
from django.http import HttpResponse

from MyMessage.models import Message


def index_page_view(request):
    return render(request, 'index.html')

def translate_page_view(request):
    return HttpResponse('translate_list_view')

def studentinfo_page_view(request):
    return HttpResponse('student info')
