from django.db import models
from django.contrib.auth.models import User


class GameScore(models.Model):
    GAME_CHOICES = [
        ("anagram", "Anagram Hunt"),
        ("math", "Math Facts Practice"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=20, choices=GAME_CHOICES)
    settings = models.CharField(max_length=255)
    time_finished = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.game_type} - {self.score}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - Review"