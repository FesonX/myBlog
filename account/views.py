from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm


def user_login(request):
    # If POST Validate data, if GET, send a login page
    if request.method == 'POST':
        # Get POST data from frontend
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # cleaned_data will return valid data as a dict, ignore invalid property
            cd = login_form.cleaned_data
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


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return HttpResponse("Register Successfully")
        else:
            return HttpResponse("Sorry, failed to register")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {"form": user_form,
                                                         'profile': userprofile_form})
