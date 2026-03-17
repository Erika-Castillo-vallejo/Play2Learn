from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from games.models import Review
from .forms import ContactForm
from .forms import ContactForm, AccountUpdateForm


def home(request):
    reviews = Review.objects.filter(featured=True).order_by("-created_at")[:5]

    return render(
        request,
        "core/index.html",
        {"reviews": reviews}
    )


def login_page(request):
    return render(request, "core/login.html")


def about(request):
    return render(request, "core/about.html")


def anagram(request):
    return render(request, "core/anagram.html")


def anagram_play(request):
    return render(request, "core/anagram-play.html")


def anagram_timesup(request):
    return render(request, "core/anagram-timesup.html")


def math(request):
    return render(request, "core/math.html")


def addition(request):
    return render(request, "core/addition.html")


def subtraction(request):
    return render(request, "core/subtraction.html")


def multiplication(request):
    return render(request, "core/multiplication.html")


def division(request):
    return render(request, "core/division.html")


def math_timesup(request):
    return render(request, "core/math-timesup.html")


def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_message = f"""
Message from Play2Learn Contact Form

From: {email}
Subject: {subject}

Message:
{message}
"""

            send_mail(
                subject=f"Play2Learn Contact: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form, "success": success})


@login_required
def account(request):
    profile = request.user.profile

    if request.method == "POST":
        form = AccountUpdateForm(request.POST)

        if form.is_valid():
            request.user.first_name = form.cleaned_data["first_name"]
            request.user.last_name = form.cleaned_data["last_name"]
            request.user.email = form.cleaned_data["email"]
            request.user.save()

            profile.first_name = form.cleaned_data["first_name"]
            profile.last_name = form.cleaned_data["last_name"]
            profile.phone = form.cleaned_data["phone"]
            profile.account_type = form.cleaned_data["account_type"]
            profile.age = form.cleaned_data["age"]
            profile.referrer = form.cleaned_data["referrer"]
            profile.save()

            return render(
                request,
                "core/account.html",
                {
                    "form": form,
                    "success": True
                }
            )
    else:
        form = AccountUpdateForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "phone": profile.phone,
                "account_type": profile.account_type,
                "age": profile.age,
                "referrer": profile.referrer,
            }
        )

    return render(request, "core/account.html", {"form": form})