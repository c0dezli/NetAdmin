from django.conf.urls import url, patterns
from . import views
from MyMessage.views import message_detail_view, compose_message_view, message_list_view

urlpatterns = patterns(
    '',

    (r'^$', views.index_page_view),

    (r'^tota/$', message_list_view, {'con_type': 2}),

    (r'^tota/new/$', compose_message_view),
    (r'^tota/(?P<conversation_id>[0-9]+)/$', message_detail_view),

    (r'^toparents/$', message_list_view, {'con_type': 3}),

    (r'^toparents/(?P<conversation_id>[0-9]+)/$', message_detail_view),
    (r'^toparents/new/$', compose_message_view),

    (r'^tostudent/$', message_list_view, {'con_type': 1}),
    (r'^tostudent/new/$', compose_message_view),
    (r'^tostudent/(?P<conversation_id>[0-9]+)/$', message_detail_view),

    (r'^translate/$', views.translate_page_view),
    (r'^studentinfo/$', views.studentinfo_page_view),
    )
