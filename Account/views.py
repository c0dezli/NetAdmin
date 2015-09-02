# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

from forms import MyRegistrationForm, ChangeInfoFrom, UploadFileForm
from .models import Account

def LoginView(request):
    '''
    Login View
    '''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/index/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def LogoutView(request):
    '''
    Log the user out
    '''
    auth_logout(request)
    return HttpResponseRedirect('/account/login/')


def RegisterView(request):
    if request.method == 'POST':
        form = MyRegistrationForm(data=request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = MyRegistrationForm()
        print 'the form submit error'

    #args = {}
    #args.update(csrf(request))
    #args['form'] = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})

def ProfileView(request):
    return render(request, 'profile.html')

def ChangeInfoView(request):
    if request.user.is_authenticated() and request.method == 'POST':
        #try:
        request.user.whatsup = request.POST['whatsup']
        request.user.username = request.POST['username']
        request.user.school = request.POST['school']
        request.user.sex = request.POST['sexRadios']
        request.user.phone = request.POST['phone']
        request.user.save()
        #except:
        #    pass
        return HttpResponseRedirect('/account/profile/')


#def ChangePassView(request):
#    if request.user.is_authenticated() and request.method == 'POST':

def ChangeAvatarView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Account(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/account/url/')
    else:
        form = UploadFileForm()
    return render_to_response('profile.html', {'form': form})

