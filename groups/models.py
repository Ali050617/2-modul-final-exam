from django.db import models
from teachers.models import Teacher
from subjects.models import Subject


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='groups', null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='group_subjects')

    def __str__(self):
        return self.name
