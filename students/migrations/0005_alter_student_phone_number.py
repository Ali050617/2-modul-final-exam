# Generated by Django 5.1.5 on 2025-02-11 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(help_text='Enter a valid Uzbekistan phone number (e.g., +998901234567).', max_length=13, validators=[django.core.validators.RegexValidator(message='Enter a valid Uzbekistan phone number in the format: +998XXXXXXXXX (9 digits after +998).', regex='^\\+998\\d{9}$')]),
        ),
    ]
