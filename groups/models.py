from django.db import models
from django.urls import reverse

from subjects.models import Subject
from teachers.models import Teacher


class Group(models.Model):
    GRADE_LEVEL_CHOICES = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    SCHEDULE_CHOICES = [
        ('mr', 'Morning Session'),
        ('af', 'Afternoon Session'),
        ('ev', 'Evening Session'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups', blank=True)
    schedule = models.CharField(max_length=2, choices=SCHEDULE_CHOICES)
    academic_year = models.CharField(max_length=30)
    max_students = models.PositiveIntegerField()
    description = models.TextField()
    subjects = models.ManyToManyField(Subject, related_name='groups')

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def __str__(self):
        return self.name


