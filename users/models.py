from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from departments.base_models import BaseModel


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class UserProfile(BaseModel):
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')