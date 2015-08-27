from django.shortcuts import render
from django.http import HttpResponse

def email_page_view(request):
    return render(request, 'mailbox.html')

def toparents_page_view(request):
    return HttpResponse('toparents')

def tota_page_view(request):
    return HttpResponse('toTA')

def toadmin_page_view(request):
    return HttpResponse('toadmin')

def toprof_page_view(request):
    return HttpResponse('toprof')
