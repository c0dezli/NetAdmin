from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView, name='login'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^register/$', views.RegisterView, name='register'),
]