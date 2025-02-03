from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from departments.models import Department
from users.models import CustomUser
from subjects.models import Subject


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='teachers', null=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    qualification = models.CharField(max_length=100)
    join_date = models.DateField()
    employment_type = models.CharField(
        max_length=20,
        choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')],
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Yangi qo‘shildi

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('teachers:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.user.username}-{self.pk if self.pk else self.email}")
        super().save(*args, **kwargs)
