from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

app_name = 'users'

urlpatterns = [
	url(r'^$', views.user_view, name ='index'),
	url(r'^main/$', views.main_view, name='main'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^recharge/$', views.recharge_view, name='recharge'),
	url(r'^logout/$', views.logout_view, name="logout"),

]
