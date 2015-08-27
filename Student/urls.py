from django.conf.urls import url
from . import views
from MyMessage.views import compose_message_view,message_detail_view

urlpatterns = [
    url(r'^$', views.index_page_view),
    url(r'^email/', views.index_page_view),

    url(r'^toadmin/$', views.toadmin_page_view),
    url(r'^toadmin/new/$', compose_message_view),
    url(r'^toadmin/([0-9]+)/$', message_detail_view),

    url(r'^tota/$', views.tota_page_view),
    url(r'^tota/new/$', compose_message_view),
    url(r'^tota/([0-9]+)/$', message_detail_view),

    url(r'^toparents/$', views.toparents_page_view),
    url(r'^toparents/new/$', compose_message_view),
    url(r'^toparents/([0-9]+)/$', message_detail_view),

    url(r'^toprof/$', views.toprof_page_view),
    url(r'^toprof/new/$', compose_message_view),
    url(r'^toprof/([0-9]+)/$', message_detail_view),

]