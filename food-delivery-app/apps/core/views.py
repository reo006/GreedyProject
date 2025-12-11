from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_edit_view(request):
    # This view will handle profile editing
    return render(request, 'accounts/profile_edit.html')

def search_view(request):
    # This view will handle product searching
    return render(request, 'restaurants/search.html')

def order_confirm_view(request):
    # This view will handle order confirmation
    return render(request, 'orders/confirm.html')