from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password

from .models import CustomUser, UserProfile


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "name": "email",
                "type": "email",
                "required": True,
                'placeholder': "name@school.com",
                'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "name": "password",
                'placeholder': 'Enter your password',
                'class': 'block w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            }
        )
    )
    remember_me = forms.BooleanField(required=False)


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
    )

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-md'})
    )

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="New Password"
    )

    repeat_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="Repeat Password"
    )

    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date', 'phone_number')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['username'].initial = user.username

        for field_name in self.fields:
            if field_name not in ["birth_date", "new_password", "repeat_password"]:
                self.fields[field_name].widget.attrs.update({
                    'class': 'w-full px-3 py-2 border rounded-md'
                })

        self.fields['bio'].widget.attrs.update({'rows': '4'})

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        repeat_password = cleaned_data.get("repeat_password")

        if new_password or repeat_password:
            if new_password != repeat_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")

        if new_password:
            user_profile.user.password = make_password(new_password)
            user_profile.user.save()

        username = self.cleaned_data.get("username")
        if username:
            user_profile.user.username = username
            user_profile.user.save()

        if commit:
            user_profile.save()

        return user_profile
