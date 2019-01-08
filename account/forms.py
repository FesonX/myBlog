from django import forms


class LoginForm(forms.Form):
    # attrs for style
    # reference: https://docs.djangoproject.com/en/2.1/ref/forms/widgets/
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # set input type as password
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
