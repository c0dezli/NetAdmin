from django.conf.urls import url
from . import views
from MyMessage.views import message_detail_view, compose_message_view, message_list_view

urlpatterns = [
    url(r'^$', views.index_page_view),

    url(r'^tota/$', message_list_view),
    url(r'^tota/new/$', compose_message_view),
    url(r'^tota/(?P<conversation_id>[0-9]+)/$', message_detail_view),

    # todo: find the wawy to call view function manually
    url(r'^toparentst/$', message_list_view, {'type': 3}),
    url(r'^toparents/(?P<conversation_id>[0-9]+)/$', message_detail_view),
    url(r'^toparents/new/$', compose_message_view),

    url(r'^tostudent/$',message_list_view),
    url(r'^tostudent/new/$', compose_message_view),
    url(r'^tostudent/(?P<conversation_id>[0-9]+)/$', message_detail_view),

    url(r'^translate/$', views.translate_page_view),
    url(r'^studentinfo/$', views.studentinfo_page_view),
]
