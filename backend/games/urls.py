from django.urls import path
from . import views

urlpatterns = [
    path("save-score/", views.save_score, name="save_score"),
    path("my-scores/", views.my_scores, name="my_scores"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("leave-review/", views.leave_review, name="leave_review"),
]