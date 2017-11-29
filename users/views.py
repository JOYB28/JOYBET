from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Match, UserProfile, Comment, Team


# Create your views here.
class IndexView(TemplateView): # TemplateView를 상속 받는다.
	template_name = 'users/index.html'

class SignUpForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())
	team = forms.ModelChoiceField(queryset=Team.objects.all())

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", required=True, max_length=30)
	password = forms.CharField(label="Password", required=True, max_length=30,
		widget = forms.PasswordInput())

def user_view(request):
	if request.user.is_authenticated :
		return render(request, 'users/index.html', {'user' : request.user, 'match': Match.objects.all()})
	else:	
		return redirect('/login/')

def signup_view(request):
	if request.method == 'POST':
		# 서버한테 정보를 보내서, 아이디를 만들어주는 부분

		if User.objects.filter(username=request.POST['username']).exists():
			form = SignUpForm()

			return render(request, 'users/signup.html', {'form': form, 'errors': 'ID 중복'}) 

		user = User.objects.create_user(
			username=request.POST['username'],
			password=request.POST['password'],
			email='',
		)
		# save UserProfile
		profile = UserProfile(user=user)
		profile.last_recharge = timezone.now()
		profile.game_money = 50000
		profile.prefer_team = Team.objects.get(id=request.POST['team'])
		profile.save()

		login(request, authenticate(
			username=request.POST['username'],
			password=request.POST['password'],
		))

		#return HttpResponseRedirect('/')
		#return HttpResponseRedirect(reverse_lazy("login_done"))
		return render(request, 'users/index.html', {'user' : user})

	elif request.method == 'GET':
		# 서버한테 아이디를 만들기 위한 폼을 받아오는 부분
		form = SignUpForm()

		return render(request, 'users/signup.html', {'form': form, })

def main_view(request):
	#logout(request)
	username = password = ''
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
		return redirect('/')

	elif request.method == 'GET':
		form = SignUpForm()
		return render(request, 'users/login.html', {'form': form})



def logout_view(request):
	logout(request)
	form = SignUpForm()
	return redirect('/users/')
	return render(request, 'users/login.html', {'form': form})

def recharge_view(request):
	user = request.user
	now = timezone.now()
	if now >= user.userprofile.last_recharge + timedelta(minutes=1):
		user.userprofile.game_money += 50000
		user.userprofile.last_recharge = now
		user.userprofile.can_recharge = now + timedelta(minutes=1)
		user.userprofile.save()
		return redirect('/users/')
	else:
		return redirect('/users/')









