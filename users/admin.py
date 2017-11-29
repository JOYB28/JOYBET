from django.contrib import admin
from .models import Match, UserProfile, Comment, Team, Bet

# Register your models here.
admin.site.register(Match)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Team)
admin.site.register(Bet)