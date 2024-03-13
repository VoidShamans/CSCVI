from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Retrieve username and password from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the credentials are valid
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If valid, log the user in and redirect to the home page
            login(request, user)
            return redirect(reverse('home'))  # Assuming 'home' is the name of the URL pattern for your home page
        else:
            # If invalid, render the login page again with an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Render the login form
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'web_project/Home.html')

def video(request):
    return render(request, 'web_project/Video.html')

@login_required
def discussion(request):
    return render(request, 'web_project/Discussion.html')

def sign_out(request):
    logout(request)
    return redirect('home') 