from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ログインページ
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),

    # ログアウト後に home に戻る設定
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),

    # 新規登録ページ
    path('signup/', views.signup, name='signup'),

    # パスワード変更（アカウント情報編集）
    path('profile/edit/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/profile_edit.html',
        success_url='/'
    ), name='profile_edit'),
]
