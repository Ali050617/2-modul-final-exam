from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, FormView
from django.shortcuts import render
from .models import UserProfile
from .forms import UserProfileForm, CustomAuthenticationForm

User = get_user_model()


class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)


class UserLogoutView(View):
    next_page = 'users:login'

    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile-update.html'
    login_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
