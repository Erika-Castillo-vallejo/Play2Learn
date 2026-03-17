from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("account/", views.account, name="account"),
]