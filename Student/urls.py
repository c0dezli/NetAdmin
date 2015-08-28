from django.conf.urls import url, patterns
from . import views
from MyMessage.views import compose_message_view,message_detail_view,message_list_view

urlpatterns = patterns(
    '',
    (r'^$', views.index_page_view),
    (r'^email/', views.index_page_view),

    (r'^toadmin/$', message_list_view(),{'con_type':1}),
    (r'^toadmin/new/$', compose_message_view),
    (r'^toadmin/([0-9]+)/$', message_detail_view),

    (r'^tota/$', message_list_view(),{'con_type':2}),
    (r'^tota/new/$', compose_message_view),
    (r'^tota/([0-9]+)/$', message_detail_view),

    (r'^toparents/$', message_list_view(),{'con_type':5}),
    (r'^toparents/new/$', compose_message_view),
    (r'^toparents/([0-9]+)/$', message_detail_view),

)