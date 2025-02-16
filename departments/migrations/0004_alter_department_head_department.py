# Generated by Django 5.1.5 on 2025-02-10 09:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='head_department',
            field=models.CharField(blank=True, choices=[('js', 'Dr. Jane Smith'), ('jd', 'Dr. John Doe'), ('sj', 'Prof. Sarah Johnson')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
