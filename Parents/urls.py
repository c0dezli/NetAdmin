from django.conf.urls import url, patterns
from . import views
from MyMessage.views import compose_message_view,message_detail_view,message_list_view

urlpatterns = patterns(
    '',
    (r'^$', views.email_page_view),
    (r'^email/', views.email_page_view),

    (r'^toadmin/$', message_list_view,{'con_type': 3}),
    (r'^toadmin/new/$', compose_message_view),
    (r'^toadmin/([0-9]+)/$', message_detail_view),

    (r'^tota/$', message_list_view,{'con_type':6}),
    (r'^tota/new/$', compose_message_view),
    (r'^tota/([0-9]+)/$', message_detail_view),

)
