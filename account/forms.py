from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    # set input type as password
    password = forms.CharField(widget=forms.PasswordInput)
