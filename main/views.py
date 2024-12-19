from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
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
