from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Teacher
from users.forms import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_student', 'is_teacher')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['department', 'subjects', 'qualification', 'join_date', 'employment_type']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_subjects(self):
        subjects = self.cleaned_data.get('subjects')
        if not subjects:
            raise forms.ValidationError("Please select at least one subject.")
        return subjects


