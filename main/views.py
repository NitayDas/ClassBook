from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password


def home_view(request):
    return render(request, 'auth/home.html')

# User Registration View
def register_view(request):
    preference_choices = dict(Preference._meta.get_field('name').choices)
    group_choices = dict(StudyGroup._meta.get_field('name').choices)

    selected_groups = []
    selected_preferences = []

    # If the user is a student and already has selected groups or preferences
    if request.method == 'POST':
        groups_names = request.POST.getlist('groups')
        preferences_names = request.POST.getlist('preferences')

        selected_groups = groups_names  # Store selected groups
        selected_preferences = preferences_names  # Store selected preferences
        
        print(selected_preferences)

        # Perform your user registration logic here...

    return render(request, 'auth/register.html', {
        'group_choices': group_choices,
        'preference_choices': preference_choices,
        'selected_groups': selected_groups,
        'selected_preferences': selected_preferences
    })



# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'logging successful! Welcome, {username}!')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'auth/login.html')

# User Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

# Dashboard View (Role-Based Access)
def dashboard_view(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            return render(request, 'dashboard/teacher_dashboard.html')
        elif request.user.is_student():
            return render(request, 'dashboard/student_dashboard.html')
    return redirect('login')
