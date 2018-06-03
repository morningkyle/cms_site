from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from login import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/post'}, name='logout'),
    url(r'^signup/$', views.SignUp.as_view(), {'next_page': '/post'}, name='signup'),
]
