from django.contrib import admin
from .models import GameScore, Review


@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ("user", "game_type", "score", "time_finished")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "featured", "created_at")