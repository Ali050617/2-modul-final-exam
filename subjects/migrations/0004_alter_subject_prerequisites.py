# Generated by Django 5.1.5 on 2025-02-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_alter_subject_grade_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prerequisites',
            field=models.CharField(blank=True, choices=[('math', 'Basic Mathematics'), ('physics', 'Introduction to Physics'), ('chemistry', 'Basic Chemistry'), ('english', 'English Language')], max_length=255),
        ),
    ]
