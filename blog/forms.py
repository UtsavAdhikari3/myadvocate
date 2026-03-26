from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Your Name",
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "example@email.com",
        }),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Briefly describe your legal issue (This is confidential)",
        }),
    )
