#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from Account.models import Account
from .models import Message, Conversation

# Create your views here.

def message_detail_view(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    con_type = conversation.type
    message_list = conversation.messages.all()
    # todo: notification substrction
    for message in message_list:
        if message.unread and request.user.username == message.receiver:
            message.unread = False
            message.save()
    # todo: if too many replies then split to multiple pages
    # todo: the redirect url
    return render(request, 'message_detail.html',
                  {'message_list': message_list,
                   'receiver': conversation.receiver,
                   'conversation_id': conversation_id,
                   'con_type': con_type,
                   'redirect_url': request.get_full_path(),
                   'title': conversation.title})

def send_message_view(request):
    '''
    type1 agent with student
    type2 agent with TA
    type3 agent with parents
    type4 student with TA
    type5 student with parents
    type6 TA with parents
    '''
    # user is logged in and is using POST method
    if request.user.is_authenticated() and request.method == 'POST':
        # new conversation
        try:
            # init a new conversation instance
            new_conversation = Conversation()
            new_conversation.title = request.POST['title']
            new_conversation.sender = request.POST['sender']
            new_conversation.receiver = request.POST['receiver']
            try:
                reciver = Account.objects.get(username=request.POST['receiver'])
                starter = Account.objects.get(username=request.POST['sender'])
            except:
                # todo: Throw out the reciver wrong error
                print 'asfdasfaf'
                pass

            if starter.is_admin and reciver.is_student:
                con_type = 1
            elif starter.is_admin and reciver.is_TA:
                con_type = 2
            elif starter.is_admin and reciver.is_parents:
                con_type = 3
            elif starter.is_student and reciver.is_TA:
                con_type = 4
            elif starter.is_student and reciver.is_parents:
                con_type = 5
            else:
                con_type = 6

            new_conversation.type = con_type
            new_conversation.save()
            # init a new message instance
            new_message = Message()
            new_message.receiver = request.POST['receiver']
            new_message.sender = request.POST['sender']
            new_message.content = request.POST['content']
            new_message.addfile = request.POST['File']
            #new_message.addfile.read()
            new_message.save()
            # add the new message to conversation
            new_conversation.messages.add(new_message)

            if new_conversation.type == 1 or new_conversation.type == 2 or new_conversation.type == 3:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_agent += 1
            elif new_conversation.type == 4 or new_conversation.type == 5:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_student += 1
            elif new_conversation.type == 6:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_TA += 1
            # to_be_notified_user = Account.objects.filter(Q(username=new_message.receiver))[0]
            # return to /****/****/(conversation_id)/
            return HttpResponseRedirect(request.POST['redirect_url'])

        # replying a exist conversation
        except:
            conversation_id = request.POST['conversation_id']
            # init a new message instance
            new_message = Message()
            new_message.receiver = request.POST['receiver']
            new_message.sender = request.POST['sender']
            new_message.content = request.POST['content']
            new_message.addfile = request.POST['File']
            #new_message.addfile.read()
            # save the message to DB
            new_message.save()
            # get the conversation by ID, and add the new message to the conversation
            conversation = Conversation.objects.get(id=conversation_id)
            conversation.messages.add(new_message)
            con_type = conversation.type
            if con_type == 1 or con_type == 2 or con_type == 3:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_agent += 1
            if con_type == 3 or con_type == 4:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_student += 1
            if con_type == 6:
                Account.objects.get(username=new_message.receiver).notification.new_message_from_TA += 1
            # return to /****/****/(conversation_id)/
            return HttpResponseRedirect(request.POST['redirect_url'])
    else:
        return HttpResponseRedirect('/index/')

def message_list_view(request, con_type):
    '''
    type1 agent with student
    type2 agent with TA
    type3 agent with parents
    type4 student with TA
    type5 student with parents
    type6 TA with parents
    '''

    message_list = Conversation.objects.filter(Q(type=con_type) & (Q(sender=request.user.username) | Q(receiver=request.user.username))).order_by('newest_reply_time')

    page = int(message_list.count()/10)

    if not message_list:
        no_message = True
    else:
        no_message = False

    if (con_type == 1 or con_type == 2 or con_type == 3) and (not request.user.is_admin):
        print request.user.is_admin
        message_category = '消息列表--中介'
    elif (con_type == 1 or con_type == 4 or con_type == 5) and (not request.user.is_student):
        message_category = '消息列表--学生'
    elif (con_type == 2 or con_type == 4 or con_type == 6) and (not request.user.is_TA):
        message_category = '消息列表--TA'
    else:
        message_category = '消息列表--家长'

    return render(request, 'message_list.html',
                  {'message_category': message_category,
                   'message_list': message_list,
                   'page': page,
                   'no_message': no_message})

def compose_message_view(request):
    if request.user.is_authenticated():
        return render(request, 'message_new.html')
    else:
        return HttpResponseRedirect('/account/login/')
