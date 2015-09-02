from django.db import models
from Account.models import Account
# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)
    addfile = models.FileField()

    def __unicode__(self):
        return 'From ' + self.sender


class Conversation(models.Model):
    '''
    type1 agent with student
    type2 agent with TA
    type3 agent with parents
    type4 student with TA
    type5 student with parents
    '''

    title = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    newest_reply_time = models.DateTimeField(auto_now=True)
    messages = models.ManyToManyField(Message)

    type = models.IntegerField()

    def __unicode__(self):
        return self.title
