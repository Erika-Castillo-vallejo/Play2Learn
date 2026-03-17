from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import GameScore
import json


@require_POST
@login_required
def save_score(request):
    try:
        data = json.loads(request.body)

        game_type = data.get("game_type")
        settings = data.get("settings")
        score = data.get("score")

        GameScore.objects.create(
            user=request.user,
            game_type=game_type,
            settings=settings,
            score=score,
        )

        return JsonResponse({"status": "success"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


@login_required
def my_scores(request):
    scores = GameScore.objects.filter(user=request.user).order_by("-time_finished")

    return render(
        request,
        "games/my_scores.html",
        {"scores": scores}
    )


@login_required
def leaderboard(request):
    math_all_scores = GameScore.objects.filter(game_type="math").order_by("-score", "-time_finished")
    anagram_all_scores = GameScore.objects.filter(game_type="anagram").order_by("-score", "-time_finished")

    math_scores = []
    seen_math_users = set()

    for score in math_all_scores:
        if score.user_id not in seen_math_users:
            math_scores.append(score)
            seen_math_users.add(score.user_id)

    anagram_scores = []
    seen_anagram_users = set()

    for score in anagram_all_scores:
        if score.user_id not in seen_anagram_users:
            anagram_scores.append(score)
            seen_anagram_users.add(score.user_id)

    return render(
        request,
        "games/leaderboard.html",
        {
            "math_scores": math_scores,
            "anagram_scores": anagram_scores,
        }
    )

from django.shortcuts import redirect
from .models import Review


@login_required
def leave_review(request):

    if request.method == "POST":
        review_text = request.POST.get("review_text")

        Review.objects.create(
            user=request.user,
            review_text=review_text
        )

        return redirect("home")

    return render(request, "games/leave_review.html")