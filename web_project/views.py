from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.urls import reverse
from django.contrib.auth import logout
from .models import UserMessage
from .forms import UserMessageForm


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
            return redirect(reverse('home'))  
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def home(request):
    return render(request, 'web_project/Home.html')

def video(request):
    return render(request, 'web_project/Video.html')

@login_required
def discussion(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('discussion')  
    else:
        form = UserMessageForm()

    # Retrieve and display messages for the logged-in user
    messages = UserMessage.objects.all().order_by('-created_at')
    return render(request, 'web_project/Discussion.html', {'form': form, 'messages': messages})

def edit_message(request, message_id):
    message = get_object_or_404(UserMessage, id=message_id, user=request.user)

    if request.method == 'POST':
        form = UserMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('discussion')  
    else:
        form = UserMessageForm(instance=message)

    return render(request, 'web_project/edit_message.html', {'form': form})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(UserMessage, id=message_id, user=request.user)
    message.delete()
    return redirect('discussion')

def sign_out(request):
    logout(request)
    return redirect('home') 