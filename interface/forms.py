from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LeadGeneratorForm(forms.Form):
    keywords = forms.CharField(
        label="Keywords",
        widget=forms.TextInput(
            attrs={"placeholder": "Hotel, Gym", "autocomplete": "off"}
        ),
    )
    location = forms.CharField(
        label="Location",
        widget=forms.TextInput(
            attrs={"placeholder": "Lviv, Rivne", "autocomplete": "off"}
        ),
    )
    leads_num = forms.ChoiceField(
        label="Number of Leads", choices=[(i, str(i)) for i in range(1, 201)]
    )


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
