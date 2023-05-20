from django import forms


class ShortenerForm(forms.Form):
    original_url = forms.URLField(
        label="",
        max_length=200,
        widget=forms.TextInput(
            attrs={"placeholder": "www.example.com", "class": "original-url"}
        ),
    )
