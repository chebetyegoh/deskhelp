from django import forms

from user.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","password"]

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']
        return first_name

    def clean_lastname(self):
        last_name = self.cleaned_data['last_name']
        return last_name

        

class LoginForm():
    email=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
