from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from users.models import CustomUser
from groups.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=13)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=20)
    gender = models.CharField(max_length=50)
    enrollment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  # Qo‘shildi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.user.username}-{self.pk if self.pk else self.phone_number}")
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('students:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
