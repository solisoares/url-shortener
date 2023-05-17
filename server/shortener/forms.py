from django import forms


class ShortenerForm(forms.Form):
    original_url = forms.URLField(label="Original URL", max_length=200)