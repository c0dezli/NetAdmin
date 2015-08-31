from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView, name='login'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^register/$', views.RegisterView, name='register'),
    url(r'^profile/$', views.ProfileView, name='profile'),
    url(r'^addavatar/$', views.ChangeAvatarView, name='avatar'),
    url(r'^changeinfo/$', views.ChangeInfoView)

]