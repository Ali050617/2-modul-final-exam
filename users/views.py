from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.core.mail import send_mail
from django import forms
from .models import UserProfile
from .forms import CustomUserCreationForm

User = get_user_model()


class UserSignupView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.otp = get_random_string(length=6, allowed_chars='1234567890')
        user.otp_created_at = now()
        user.save()

        send_mail(
            'Email Verification Code',
            f'Your OTP code is: {user.otp}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

        return redirect('verify_email', email=user.email)


class VerifyEmailView(CreateView):
    template_name = 'users/profile-updated.html'

    def post(self, request, *args, **kwargs):
        email = self.kwargs.get('email')
        otp = request.POST.get('otp')
        try:
            user = User.objects.get(email=email, otp=otp)
            if user.otp_created_at and (now() - user.otp_created_at).seconds < 300:
                user.is_active = True
                user.email_verified = True
                user.otp = None
                user.otp_created_at = None
                user.save()
                return redirect('login')
            else:
                return render(request, self.template_name, {'error': 'OTP expired'})
        except User.DoesNotExist:
            return render(request, self.template_name, {'error': 'Invalid OTP'})


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('dashboard')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date']


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile-update.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'
