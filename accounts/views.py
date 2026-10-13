from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard' if request.user.role == 'admin' else 'authority_dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            return redirect('authority_dashboard')
        error = 'Invalid credentials or inactive account'
    return render(request, 'accounts/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def manage_authorities(request):
    authorities = User.objects.filter(role='authority')
    return render(request, 'accounts/manage_authorities.html', {'authorities': authorities})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def register(request):
    error = None
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            error = 'Passwords do not match'
        elif User.objects.filter(username=username).exists():
            error = 'Username already taken'
        else:
            User.objects.create_user(
                username=username, password=password, email=email,
                first_name=fullname, mobile=mobile, address=address,
                role='authority',
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    return render(request, 'accounts/register.html', {'error': error})









