from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='core:home'),
        name='logout',
    ),
    path('signup/', views.signup, name='signup'),
    path(
        'profile/edit/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/profile_edit.html',
            success_url='/',
        ),
        name='profile_edit',
    ),
]

