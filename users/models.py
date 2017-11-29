from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

# team
class Team(models.Model):
	name = models.CharField(max_length=50)
	#picture = models.ImageField(upload_to=, blank=True, null=True)

	def __str__(self):
		return self.name

# match information
class Match(models.Model):
	title = models.CharField(max_length=50, default='match')
	match_round = models.PositiveIntegerField(default=0)
	home_team = models.ForeignKey('users.Team', related_name='home_team')
	away_team = models.ForeignKey('users.Team', related_name='away_team')
	date = models.DateTimeField(auto_now_add=False, blank=True)
	win = models.FloatField()
	draw = models.FloatField()
	loose = models.FloatField()
	win_bet = models.PositiveIntegerField(default=0)
	draw_bet = models.PositiveIntegerField(default=0)
	loose_bet = models.PositiveIntegerField(default=0)
	total_bet = models.PositiveIntegerField(default=0)
	is_finished = models.BooleanField()
	home_team_score = models.PositiveIntegerField(default=0)
	away_team_score = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title



# user profile with game money for betting
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	game_money = models.PositiveIntegerField(default=0)
	last_recharge = models.DateTimeField(default=timezone.now)
	can_recharge = models.DateTimeField(default=timezone.now)
	prefer_team = models.OneToOneField(Team, blank=True, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.user.username

# comments in match
class Comment(models.Model):
	match = models.ForeignKey('users.Match', related_name='comments')
	author = models.ForeignKey(UserProfile)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

# betting information
class Bet(models.Model):
	match = models.ForeignKey('users.Match', related_name="bets")
	user = models.ForeignKey(UserProfile)
	win_bet = models.PositiveIntegerField(default=0)
	draw_bet = models.PositiveIntegerField(default=0)
	loose_bet = models.PositiveIntegerField(default=0)








