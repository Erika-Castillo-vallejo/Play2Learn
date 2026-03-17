from django.contrib import admin
from django.urls import path, include
from core import views
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("games/", include("games.urls")),

    # ✅ HOME
    path("", views.home, name="home"),

    # ✅ login 
    path("login/", lambda request: redirect("account_login"), name="login"),
   
    # ✅ about
    path("about/", views.about, name="about"),

    # ✅ anagram
    path("games/anagram/", views.anagram, name="anagram"),
    path("games/anagram/play/", views.anagram_play, name="anagram_play"),
    path("games/anagram/timesup/", views.anagram_timesup),

    # ✅ math
    path("games/math/", views.math, name="math"),
    path("games/math/play/addition/", views.addition),
    path("games/math/play/subtraction/", views.subtraction),
    path("games/math/play/multiplication/", views.multiplication),
    path("games/math/play/division/", views.division),
    path("games/math/timesup/", views.math_timesup),

    # ✅ contact
    path("contact/", views.contact, name="contact"),

    # ✅ account
    path("account/", views.account, name="account"),
    ]