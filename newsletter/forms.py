from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:  # meta data class for newsletter
        model = SignUp
        fields = ["full_name", "email"]


    def clean_email(self):  # Validator for edu domain
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not domain == "edu":
            raise forms.ValidationError("Please use EDU domain email")
        return email

