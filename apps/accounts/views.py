from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='パスワード')
    password2 = forms.CharField(widget=forms.PasswordInput, label='パスワード（確認）')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password2'):
            self.add_error('password2', 'パスワードが一致しません')
        return cleaned


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

