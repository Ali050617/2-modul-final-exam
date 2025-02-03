from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
import random
import string


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

    def generate_otp(self):
        return ''.join(random.choices(string.digits, k=6))

    def create_user_with_otp(self, email, username, password=None, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        otp = self.generate_otp()
        user.otp = otp
        user.otp_created_at = timezone.now()
        user.save(using=self._db)
        return user, otp