from django.shortcuts import render
from django.http import HttpResponseRedirect

def landing_page_view(request):
    return render(request, 'landing.html')

def index_page_view(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            return HttpResponseRedirect('/student/')
        elif request.user.is_TA:
            return HttpResponseRedirect('/ta/')
        elif request.user.is_admin:
            return HttpResponseRedirect('/agent/')
        elif request.user.is_parents:
            return HttpResponseRedirect('/parents/')
    else:
        return HttpResponseRedirect('/account/login/')
