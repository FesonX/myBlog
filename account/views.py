from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    # If POST Validate data, if GET, send a login page
    if request.method == 'POST':
        # Get POST data from frontend
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # cleaned_data will return valid data as a dict, ignore invalid property
            cd = login_form.cleaned_data
            # Authenticate via database, if doesn't exist, return None
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Hello! Login Successfully!")
            else:
                return HttpResponse("Sorry, username or password is wrong")
        else:
            return HttpResponse("Invalid login")

    if request.method == 'GET':
        # Create a empty login form
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


