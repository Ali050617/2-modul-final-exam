from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.core.mail import send_mail
from .models import UserProfile
from .forms import LoginForm, UserProfileForm, SignupForm

User = get_user_model()


class UserSignupView(CreateView):
    class Meta:
        model = User
        form_class = SignupForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'})

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        messages.success(self.request, "Registration completed successfully!")
        user.otp = get_random_string(length=6, allowed_chars='1234567890')
        user.otp_created_at = now()
        user.save()

    def form_invalid(self, form):
        messages.error(self.request, "Error during registration. Please check the entered data!")
        return super().form_invalid(form)

        send_mail(
            'Email Verification Code',
            f'Your OTP code is: {user.otp}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

        return redirect('verify_email', email=user.email)


class VerifyEmailView(CreateView):
    template_name = 'users/login.html'

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
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request=self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            remember_me = form.cleaned_data.get('remember_me', False)
            if not remember_me:
                self.request.session.set_expiry(0)
            messages.success(self.request, "You have successfully logged in!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid email or password. Try again!")
            return self.form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have successfully logged out!")
        return super().dispatch(request, *args, **kwargs)


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile-update.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
