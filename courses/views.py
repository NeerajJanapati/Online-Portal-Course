"""
Course Portal Views
View functions for handling user requests and rendering templates
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CourseForm, RegisterForm
from .models import Course


def home(request):
    """Display homepage with all available courses."""
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

def register_view(request):
    """Handle user registration with form validation."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """Authenticate and login users."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    """Display instructor dashboard with their courses."""
    courses = Course.objects.filter(instructor=request.user)
    context = {
        'courses': courses,
        'total_courses': courses.count()
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_course(request):
    """Create a new course (instructor only)."""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            messages.success(request, f'Course "{course.title}" added successfully!')
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def course_detail(request, course_id):
    """Display detailed information about a specific course."""
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def logout_view(request):
    """Log out the current user and redirect to homepage."""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')