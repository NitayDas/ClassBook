from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password


def home_view(request):
    return render(request, 'auth/home.html')

# User Registration View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Preference, StudyGroup

def register_view(request):
    preference_choices = dict(Preference._meta.get_field('name').choices)
    group_choices = dict(StudyGroup._meta.get_field('name').choices)

    selected_groups = []
    selected_preferences = []

    if request.method == 'POST':
        groups_names = request.POST.getlist('groups')
        preferences_names = request.POST.getlist('preferences')

        selected_groups = groups_names  
        selected_preferences = preferences_names 

        # Ensure that the password fields match
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'auth/register.html', {
                'group_choices': group_choices,
                'preference_choices': preference_choices,
                'selected_groups': selected_groups,
                'selected_preferences': selected_preferences
            })

        # Create the user
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')

        # Create user instance
        user = get_user_model()(username=username, email=email)
        user.set_password(password)
        user.save()
        
        user.role = role
        user.save()


        if role == 'student':
            groups = StudyGroup.objects.filter(name__in=groups_names)
            preferences = Preference.objects.filter(name__in=preferences_names)

            # user.groups.set(groups)
            # user.preferences.set(preferences)

        # Optionally, send an email or perform any additional logic here

        # Redirect to login page after successful registration
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

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
    return redirect('home')

# Dashboard View (Role-Based Access)
def dashboard_view(request):
    if request.user.is_authenticated:
        if request.user.is_teacher():
            return render(request, 'dashboard/teacher_dashboard.html')
        elif request.user.is_student():
            return render(request, 'dashboard/student_dashboard.html')
    return redirect('login')
