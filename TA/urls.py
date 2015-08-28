from django.conf.urls import url,patterns
from . import views
from MyMessage.views import message_detail_view, compose_message_view,message_list_view

urlpatterns = patterns(
    '',
    (r'^$', views.index_page_view),

    (r'^toadmin/$', message_list_view,{'con_type':2}),
    (r'^toadmin/new/$', compose_message_view),

    (r'^toadmin/([0-9]+)/$', message_detail_view),
    (r'^toadmin/new/$', compose_message_view),

    (r'^papers/$', views.papers_page_view),
    (r'^finishedpapers/$', views.finishedpapers_page_view),

    (r'^tostudent/$', message_list_view,{'con_type':4}),
    (r'^toparents/new/$', compose_message_view),
    (r'^tostudent/([0-9]+)/$', message_detail_view),
)