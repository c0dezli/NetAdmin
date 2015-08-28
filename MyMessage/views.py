#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from Account.models import Account
from .models import Message, Conversation

# Create your views here.

def message_detail_view(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    message_list = conversation.messages.all()
    for message in message_list:
        if message.unread and request.user.username == message.receiver:
            message.unread = False
            message.save()
    # todo: if too many replies then split to multiple pages
    # todo: the redirect url
    return render(request, 'message_detail.html', {'message_list': message_list, 'receiver': conversation.receiver})

def message_list_view(request, con_type):
    '''
    type1 agent with student
    type2 agent with TA
    type3 agent with parents
    type4 student with TA
    type5 student with parents
    type6 TA with parents
    '''
    print con_type
    message_list = Conversation.objects.filter(Q(type=con_type) & Q(sender=request.user.username)
                                                   | Q(receiver=request.user.username)).order_by('newest_reply_time')

    page = int(message_list.count()/10)

    if con_type == 1 or con_type == 2 or con_type == 3 and not request.user.is_admin:
        message_category = '消息列表--中介'
    elif con_type == 1 or con_type == 4 or con_type == 5 and not request.user.is_student:
        message_category = '消息列表--学生'
    elif con_type == 2 or con_type == 4 or con_type == 6 and not request.user.is_TA:
        message_category = '消息列表--TA'
    else:
        message_category = '消息列表--家长'

    return render(request, 'message_list.html',
                  {'message_category': message_category,
                   'message_list': message_list,
                   'page': page})

def compose_message_view(request):
    if request.user.is_authenticated():
        return render(request, 'message_new.html')
    else:
        return HttpResponseRedirect('/account/login/')

def send_message_view(request, which_conversation, type):
    '''
    POST: reciver, sender, content, redirect_url, (title), (reply_to)
    :param redirect_url:
    '''
    if request.user.is_authenticated() and request.method == 'POST':

        if which_conversation == 0:
            new_conversation = Conversation()

            new_conversation.title = request.POST['title']
            new_conversation.p1 = request.POST['sender']
            new_conversation.p2 = request.POST['receiver']
            new_conversation.starter = request.POST['sender']
            new_conversation.type = type
            new_conversation.save()

            new_message = Message()

            new_message.receiver = request.POST['receiver']
            new_message.sender = request.POST['sender']
            new_message.content = request.POST['content']

            new_message.save()

            return HttpResponse('send success')

        else:

            new_message = Message()
            new_message.receiver = request.POST['receiver']
            new_message.sender = request.POST['sender']
            new_message.content = request.POST['content']

            new_message.save()

            conversation = Conversation.objects.get(id=which_conversation)
            conversation.messages.add(new_message)
            # todo: notifications

            return HttpResponse('send success')
    else:
        return HttpResponseRedirect('/index/')
