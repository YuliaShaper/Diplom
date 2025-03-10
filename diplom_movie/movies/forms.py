from django import forms

from .models import Reviews


class ReviewFrom(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
