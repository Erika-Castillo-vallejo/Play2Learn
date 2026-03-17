from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20, required=False)

    account_type = forms.ChoiceField(
        choices=[
            ("personal", "Personal account"),
            ("business", "Business account"),
        ]
    )

    age = forms.IntegerField(required=False)
    referrer = forms.CharField(required=False)

    def save(self, request):
        user = super().save(request)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        profile = user.profile
        profile.first_name = self.cleaned_data["first_name"]
        profile.last_name = self.cleaned_data["last_name"]
        profile.phone = self.cleaned_data["phone"]
        profile.account_type = self.cleaned_data["account_type"]
        profile.age = self.cleaned_data["age"]
        profile.referrer = self.cleaned_data["referrer"]
        profile.save()

        return user


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)


class AccountUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=20, required=False)

    account_type = forms.ChoiceField(
        choices=[
            ("personal", "Personal account"),
            ("business", "Business account"),
        ],
        required=False
    )

    age = forms.IntegerField(required=False)
    referrer = forms.CharField(required=False)