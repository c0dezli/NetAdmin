from django.conf.urls import url
from . import views
from MyMessage.views import message_detail_view, compose_message_view

urlpatterns = [
    url(r'^$', views.index_page_view),

    url(r'^toadmin/$', views.toadmin_page_view),
    url(r'^toadmin/new/$', compose_message_view),

    url(r'^toadmin/([0-9]+)/$', message_detail_view),
    url(r'^toadmin/new/$', compose_message_view),

    url(r'^papers/$', views.papers_page_view),
    url(r'^finishedpapers/$', views.finishedpapers_page_view),

    url(r'^tostudent/$', views.tostudent_page_view),
    url(r'^toparents/new/$', compose_message_view),
    url(r'^tostudent/([0-9]+)/$', message_detail_view),
]